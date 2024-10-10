from datetime import timedelta

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from fastapi_login import LoginManager
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from db.base import Base, get_db_session


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


# Pydantic Models for requests
class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# Secret key for signing the session tokens
SECRET = "your-secret-key"

# LoginManager setup
manager = LoginManager(SECRET, token_url="/auth/login", use_header=False, use_cookie=True, cookie_name="auth_session")

# CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Load user by username
def load_user(auth_session: str | None = Cookie(None), db: Session = Depends(get_db_session)):
    payload = manager._get_payload(auth_session)
    username = payload.get("sub")
    return db.query(User).filter(User.username == username).first()


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db_session)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


@auth_router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db_session), response: Response = None):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create a session token and set it as a cookie
    access_token = manager.create_access_token(data={"sub": db_user.username}, expires=timedelta(mins=60))
    manager.set_cookie(response, access_token)
    return {"message": "Login successful"}

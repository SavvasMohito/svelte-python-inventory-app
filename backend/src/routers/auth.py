from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from fastapi_login import LoginManager
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship

from db.base import Base, get_db_session


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    items = relationship("Item", back_populates="user")


# Pydantic Models for requests
class UserAuth(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str


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


auth_router = APIRouter(prefix="/auth")
DBSession = Annotated[Session, Depends(get_db_session)]


# Load user by username
def load_user(db: DBSession, auth_session: str | None = Cookie(None)):
    payload = manager._get_payload(auth_session)
    if not payload:
        raise manager.not_authenticated_exception
    username = payload.get("sub")
    return db.query(User).filter(User.username == username).first()


@auth_router.post("/register")
def register(user: UserAuth, db: DBSession):
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
def login(user: UserAuth, db: DBSession, response: Response = None):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create a session token and set it as a cookie
    access_token = manager.create_access_token(data={"sub": db_user.username}, expires=timedelta(hours=12))
    manager.set_cookie(response, access_token)
    return {"message": "Login successful"}


@auth_router.get("/session")
def session(user: UserRead = Depends(load_user)):
    return UserRead(id=user.id, username=user.username)

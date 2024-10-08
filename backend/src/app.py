from fastapi import APIRouter, Cookie, Depends, FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from fastapi_login import LoginManager
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Database Configuration
DATABASE_URL = "postgresql://backend:backend@backend-db/backend"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI(
    title="backend",
    # version=metadata.version("backend"),
    # lifespan=lifespan_setup,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    default_response_class=UJSONResponse,
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# Secret key for signing the session tokens
SECRET = "your-secret-key"

# LoginManager setup
manager = LoginManager(SECRET, token_url="/auth/login", use_header=False, use_cookie=True, cookie_name="auth_session")


# Pydantic Models for requests
class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# Dependency for getting the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    return "hello from the backend!"


# Load user by username
def load_user(auth_session: str | None = Cookie(None)):
    db = SessionLocal()
    payload = manager._get_payload(auth_session)
    username = payload.get("sub")
    return db.query(User).filter(User.username == username).first()


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
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
def login(user: UserLogin, db: Session = Depends(get_db), response: Response = None):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create a session token and set it as a cookie
    access_token = manager.create_access_token(data={"sub": db_user.username})
    manager.set_cookie(response, access_token)
    return {"message": "Login successful"}


@auth_router.post("/logout")
def logout(response: dict = None):
    response = response or {"message": "Logged out"}
    manager.delete_cookie(response)
    return response


app.include_router(auth_router)


@app.get("/protected")
def protected_route(auth_session: str | None = Cookie(None), user=Depends(load_user)):
    return {"message": f"Hello, {user.username}. You are logged in!"}

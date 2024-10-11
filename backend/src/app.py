from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base
from routers.auth import auth_router
from routers.items import items_router

# Database Configuration
DATABASE_URL = "postgresql://backend:backend@backend-db/backend"


@asynccontextmanager
async def lifespan_setup(app: FastAPI):
    app.middleware_stack = None
    # Setup db attributes in app state
    engine = create_engine(DATABASE_URL)
    session_factory = sessionmaker(
        engine,
        expire_on_commit=False,
        # autoflush=False,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory
    # Create schema tables
    Base.metadata.create_all(app.state.db_engine)
    app.middleware_stack = app.build_middleware_stack()
    yield
    app.state.db_engine.dispose()


# FastAPI setup
app = FastAPI(
    title="backend",
    lifespan=lifespan_setup,
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

# Add auth router
app.include_router(auth_router)
app.include_router(items_router)


@app.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    return "hello from the backend!"

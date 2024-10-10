import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Session
from starlette.requests import Request

meta = sa.MetaData()


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta


def get_db_session(request: Request):
    """
    Create and get database session.

    :param request: current request.
    :yield: database session.
    """
    session: Session = request.app.state.db_session_factory()

    try:
        yield session
    finally:
        session.commit()
        session.close()

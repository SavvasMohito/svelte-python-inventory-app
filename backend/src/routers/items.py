from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship

from db.base import Base, get_db_session
from routers.auth import UserRead, load_user


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="items")
    name = Column(String)
    description = Column(String)
    quantity = Column(String)
    date = Column(String)


# Pydantic Models for requests
class ItemDelete(BaseModel):
    id: int


class ItemCreate(BaseModel):
    name: str
    description: str
    quantity: str
    date: str


class ItemRead(ItemCreate):
    id: int


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[str] = None
    date: Optional[str] = None


items_router = APIRouter()
DBSession = Annotated[Session, Depends(get_db_session)]
AuthSession = Annotated[UserRead, Depends(load_user)]


@items_router.get("/items", response_model=list[ItemRead])
def get_items(user: AuthSession, db: DBSession):
    items = db.query(Item).filter(Item.uid == user.id).all()
    return items


@items_router.post("/items", response_model=ItemRead)
def create_item(item: ItemCreate, user: AuthSession, db: DBSession):
    try:
        new_item = Item(
            uid=user.id,
            name=item.name,
            description=item.description,
            quantity=item.quantity,
            date=item.date,
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# @items_router.patch("/items/{item_id}")
# def update_item(item: ItemUpdate, user: AuthSession, db: DBSession):
#     # Create a session token and set it as a cookie
#     access_token = manager.create_access_token(data={"sub": db_user.username}, expires=timedelta(hours=12))
#     manager.set_cookie(response, access_token)
#     return {"message": "Login successful"}


# @items_router.delete("/items/{item_id}")
# def delete_item(user: AuthSession, db: DBSession):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")

#     # Create a session token and set it as a cookie
#     access_token = manager.create_access_token(data={"sub": db_user.username}, expires=timedelta(hours=12))
#     manager.set_cookie(response, access_token)
#     return {"message": "Login successful"}

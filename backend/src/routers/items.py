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
    items = db.query(Item).filter(Item.uid == user.id).order_by(Item.id.desc()).all()
    return items


@items_router.post("/items")
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@items_router.patch("/items/{item_id}")
def update_item(item_id: str, item: ItemUpdate, user: AuthSession, db: DBSession):
    try:
        exists = db.query(Item).filter(Item.id == item_id, Item.uid == user.id).first()
        if not exists:
            raise HTTPException(status_code=404, detail="Item not found")
        db.query(Item).filter(Item.id == item_id, Item.uid == user.id).update(item.model_dump())
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@items_router.delete("/items/{item_id}")
def delete_item(item_id: str, user: AuthSession, db: DBSession):
    try:
        item = db.query(Item).filter(Item.id == item_id, Item.uid == user.id).first()
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        db.delete(item)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

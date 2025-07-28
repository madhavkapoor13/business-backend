from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import item_type as models
from schemas import item_type as schemas

router = APIRouter(prefix="/item-type", tags=["Item Type"])

@router.post("/", response_model=schemas.ShowItemType, status_code=status.HTTP_201_CREATED)
def create_item_type(item_type: schemas.ItemTypeCreate, db: Session = Depends(get_db)):
    db_item_type = models.ItemType(type_name=item_type.type_name)
    db.add(db_item_type)
    db.commit()
    db.refresh(db_item_type)
    return db_item_type

@router.get("/", response_model=List[schemas.ShowItemType])
def get_all_item_types(db: Session = Depends(get_db)):
    item_types = db.query(models.ItemType).all()
    return item_types

@router.get("/{type_id}", response_model=schemas.ShowItemType)
def get_item_type(type_id: int, db: Session = Depends(get_db)):
    item_type = db.query(models.ItemType).filter(models.ItemType.type_id == type_id).first()
    if not item_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Type not found")
    return item_type
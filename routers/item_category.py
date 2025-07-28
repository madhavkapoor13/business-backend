from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import item_category as models
from schemas import item_category as schemas

router = APIRouter(prefix="/item-category", tags=["Item Category"])

@router.post("/", response_model=schemas.ShowItemCategory, status_code=status.HTTP_201_CREATED)
def create_item_category(category: schemas.ItemCategoryCreate, db: Session = Depends(get_db)):
    db_category = models.ItemCategory(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=List[schemas.ShowItemCategory])
def get_all_item_categories(db: Session = Depends(get_db)):
    categories = db.query(models.ItemCategory).all()
    return categories

@router.get("/{category_id}", response_model=schemas.ShowItemCategory)
def get_item_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.ItemCategory).filter(models.ItemCategory.category_id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Category not found")
    return category
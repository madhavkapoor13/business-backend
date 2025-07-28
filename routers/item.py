from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import item as models
from models import item_category as category_models
from models import item_type as type_models
from models import item_expense_type as expense_type_models
from schemas import item as schemas

router = APIRouter(prefix="/item", tags=["Item"])

@router.post("/", response_model=schemas.ShowItem, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    # Validate foreign keys
    category = db.query(category_models.ItemCategory).filter(category_models.ItemCategory.category_id == item.category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Item Category with ID {item.category_id} does not exist."
        )
    item_type = db.query(type_models.ItemType).filter(type_models.ItemType.type_id == item.type_id).first()
    if not item_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Item Type with ID {item.type_id} does not exist."
        )
    expense_type = db.query(expense_type_models.ItemExpenseType).filter(expense_type_models.ItemExpenseType.expense_type_id == item.expense_type_id).first()
    if not expense_type:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Item Expense Type with ID {item.expense_type_id} does not exist."
        )

    db_item = models.Item(
        item_name=item.item_name,
        category_id=item.category_id,
        type_id=item.type_id,
        expense_type_id=item.expense_type_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[schemas.ShowItem])
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@router.get("/{item_id}", response_model=schemas.ShowItem)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
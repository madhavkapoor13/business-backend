from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import item_expense_type as models
from schemas import item_expense_type as schemas

router = APIRouter(prefix="/item-expense-type", tags=["Item Expense Type"])

@router.post("/", response_model=schemas.ShowItemExpenseType, status_code=status.HTTP_201_CREATED)
def create_item_expense_type(expense_type: schemas.ItemExpenseTypeCreate, db: Session = Depends(get_db)):
    db_expense_type = models.ItemExpenseType(expense_type_name=expense_type.expense_type_name)
    db.add(db_expense_type)
    db.commit()
    db.refresh(db_expense_type)
    return db_expense_type

@router.get("/", response_model=List[schemas.ShowItemExpenseType])
def get_all_item_expense_types(db: Session = Depends(get_db)):
    expense_types = db.query(models.ItemExpenseType).all()
    return expense_types

@router.get("/{expense_type_id}", response_model=schemas.ShowItemExpenseType)
def get_item_expense_type(expense_type_id: int, db: Session = Depends(get_db)):
    expense_type = db.query(models.ItemExpenseType).filter(models.ItemExpenseType.expense_type_id == expense_type_id).first()
    if not expense_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Expense Type not found")
    return expense_type
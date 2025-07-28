from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import financial_quarter as models
from schemas import financial_quarter as schemas

router = APIRouter(prefix="/financial-quarter", tags=["Financial Quarter"])

@router.post("/", response_model=schemas.ShowFinancialQuarter, status_code=status.HTTP_201_CREATED)
def create_financial_quarter(quarter: schemas.FinancialQuarterCreate, db: Session = Depends(get_db)):
    db_quarter = models.FinancialQuarter(quarter_name=quarter.quarter_name)
    db.add(db_quarter)
    db.commit()
    db.refresh(db_quarter)
    return db_quarter

@router.get("/", response_model=List[schemas.ShowFinancialQuarter])
def get_all_financial_quarters(db: Session = Depends(get_db)):
    quarters = db.query(models.FinancialQuarter).all()
    return quarters

@router.get("/{quarter_id}", response_model=schemas.ShowFinancialQuarter)
def get_financial_quarter(quarter_id: int, db: Session = Depends(get_db)):
    quarter = db.query(models.FinancialQuarter).filter(models.FinancialQuarter.quarter_id == quarter_id).first()
    if not quarter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Financial Quarter not found")
    return quarter
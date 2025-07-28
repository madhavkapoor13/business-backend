from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import financial_year as models
from schemas import financial_year as schemas

router = APIRouter(prefix="/financial-year", tags=["Financial Year"])

@router.post("/", response_model=schemas.ShowFinancialYear, status_code=status.HTTP_201_CREATED)
def create_financial_year(year: schemas.FinancialYearCreate, db: Session = Depends(get_db)):
    db_year = models.FinancialYear(start_year=year.start_year, end_year=year.end_year)
    db.add(db_year)
    db.commit()
    db.refresh(db_year)
    return db_year

@router.get("/", response_model=List[schemas.ShowFinancialYear])
def get_all_financial_years(db: Session = Depends(get_db)):
    years = db.query(models.FinancialYear).all()
    return years

@router.get("/{year_id}", response_model=schemas.ShowFinancialYear)
def get_financial_year(year_id: int, db: Session = Depends(get_db)):
    year = db.query(models.FinancialYear).filter(models.FinancialYear.financial_year_id == year_id).first()
    if not year:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Financial Year not found")
    return year
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import department as models
from models import entity as entity_models # Import entity model to check FK
from schemas import department as schemas

router = APIRouter(prefix="/department", tags=["Department"])

@router.post("/", response_model=schemas.ShowDepartment, status_code=status.HTTP_201_CREATED)
def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    # Validate entity_id exists
    entity = db.query(entity_models.Entity).filter(entity_models.Entity.entity_id == department.entity_id).first()
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Entity with entity_id {department.entity_id} does not exist."
        )

    db_department = models.Department(
        department_name=department.department_name,
        entity_id=department.entity_id
    )
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

@router.get("/", response_model=List[schemas.ShowDepartment])
def get_all_departments(db: Session = Depends(get_db)):
    departments = db.query(models.Department).all()
    return departments

@router.get("/{department_id}", response_model=schemas.ShowDepartment)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(models.Department).filter(models.Department.department_id == department_id).first()
    if not department:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return department
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from database.db import get_db
from models import gl_code as models
from schemas import gl_code as schemas

router = APIRouter(prefix="/gl-code", tags=["GL Code"])

@router.post("/", response_model=schemas.ShowGLCode, status_code=status.HTTP_201_CREATED)
def create_gl_code(gl_code: schemas.GLCodeCreate, db: Session = Depends(get_db)):
    db_gl_code = models.GLCode(gl_code=gl_code.gl_code, description=gl_code.description)
    db.add(db_gl_code)
    db.commit()
    db.refresh(db_gl_code)
    return db_gl_code

@router.get("/", response_model=List[schemas.ShowGLCode])
def get_all_gl_codes(db: Session = Depends(get_db)):
    gl_codes = db.query(models.GLCode).all()
    return gl_codes

@router.get("/{gl_code_id}", response_model=schemas.ShowGLCode)
def get_gl_code(gl_code_id: int, db: Session = Depends(get_db)):
    gl_code = db.query(models.GLCode).filter(models.GLCode.gl_code_id == gl_code_id).first()
    if not gl_code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="GL Code not found")
    return gl_code
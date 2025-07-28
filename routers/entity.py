from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models import entity as models
from schemas import entity as schemas

router = APIRouter(prefix="/entity", tags=["Entity"])

@router.post("/", response_model=schemas.ShowEntity, status_code=status.HTTP_201_CREATED)
def create_entity(entity: schemas.EntityCreate, db: Session = Depends(get_db)):
    db_entity = models.Entity(entity_name=entity.entity_name)
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

@router.get("/", response_model=List[schemas.ShowEntity])
def get_all_entities(db: Session = Depends(get_db)):
    entities = db.query(models.Entity).all()
    return entities

@router.get("/{entity_id}", response_model=schemas.ShowEntity)
def get_entity(entity_id: int, db: Session = Depends(get_db)):
    entity = db.query(models.Entity).filter(models.Entity.entity_id == entity_id).first()
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entity not found")
    return entity
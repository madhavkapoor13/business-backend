from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.provisioning import Provision
from schemas.provisioning import ProvisionBase, ShowProvision

router = APIRouter(
    prefix="/provision",
    tags=["Provisioning"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ShowProvision)
def create_provision(provision: ProvisionBase, db: Session = Depends(get_db)):
    new_prov = Provision(**provision.dict())
    db.add(new_prov)
    db.commit()
    db.refresh(new_prov)
    return new_prov

@router.get("/", response_model=list[ShowProvision])
def get_provisions(db: Session = Depends(get_db)):
    return db.query(Provision).all()

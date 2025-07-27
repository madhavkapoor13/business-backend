from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from models.consumption import Consumption
from database.db import SessionLocal
import shutil
import os

router = APIRouter(
    prefix="/consumption",
    tags=["Consumption"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def create_consumption(
    indent_id: str = Form(...),
    indent_date: str = Form(...),
    indent_amount: float = Form(...),
    po_date: str = Form(...),
    po_amount: float = Form(...),
    po_file: UploadFile = File(...),
    invoice_date: str = Form(...),
    invoice_amount: float = Form(...),
    invoice_file: UploadFile = File(...),
    remarks: str = Form(...),
    db: Session = Depends(get_db)
):
    # Save uploaded files
    po_path = f"{UPLOAD_DIR}/{po_file.filename}"
    invoice_path = f"{UPLOAD_DIR}/{invoice_file.filename}"

    with open(po_path, "wb") as f:
        shutil.copyfileobj(po_file.file, f)

    with open(invoice_path, "wb") as f:
        shutil.copyfileobj(invoice_file.file, f)

    record = Consumption(
        indent_id=indent_id,
        indent_date=indent_date,
        indent_amount=indent_amount,
        po_date=po_date,
        po_amount=po_amount,
        po_file=po_path,
        invoice_date=invoice_date,
        invoice_amount=invoice_amount,
        invoice_file=invoice_path,
        remarks=remarks
    )
    db.add(record)
    db.commit()
    return {"message": "Consumption added successfully"}

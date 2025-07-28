from pydantic import BaseModel

class ItemExpenseTypeCreate(BaseModel):
    expense_type_name: str

class ShowItemExpenseType(BaseModel):
    expense_type_id: int
    expense_type_name: str

    class Config:
        from_attributes = True
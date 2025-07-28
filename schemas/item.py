from pydantic import BaseModel

class ItemCreate(BaseModel):
    item_name: str
    category_id: int # Foreign key
    type_id: int     # Foreign key
    expense_type_id: int # Foreign key

class ShowItem(BaseModel):
    item_id: int
    item_name: str
    category_id: int
    type_id: int
    expense_type_id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel

class ItemCategoryCreate(BaseModel):
    category_name: str

class ShowItemCategory(BaseModel):
    category_id: int
    category_name: str

    class Config:
        from_attributes = True
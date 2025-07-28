from pydantic import BaseModel

class ItemTypeCreate(BaseModel):
    type_name: str

class ShowItemType(BaseModel):
    type_id: int
    type_name: str

    class Config:
        from_attributes = True
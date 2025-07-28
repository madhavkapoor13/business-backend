from pydantic import BaseModel

class EntityCreate(BaseModel):
    entity_name: str

class ShowEntity(BaseModel):
    entity_id: int
    entity_name: str

    class Config:
        from_attributes = True # For Pydantic v2+, use orm_mode = True for Pydantic v1
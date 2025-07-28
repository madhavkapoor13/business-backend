from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    department_name: str
    entity_id: int # Foreign key

class ShowDepartment(BaseModel):
    department_id: int
    department_name: str
    entity_id: int

    class Config:
        from_attributes = True
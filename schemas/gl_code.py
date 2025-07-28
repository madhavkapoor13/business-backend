from pydantic import BaseModel
from typing import Optional

class GLCodeCreate(BaseModel):
    gl_code: str
    description: Optional[str] = None

class ShowGLCode(BaseModel):
    gl_code_id: int
    gl_code: str
    description: Optional[str] = None

    class Config:
        from_attributes = True
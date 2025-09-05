from typing import Optional
from pydantic import BaseModel, Field
from .core.enums import CategoryType

# Category Schemas
class CategoryCreate(BaseModel):
    name: str
    type: CategoryType

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[CategoryType] = None

class SourceCreate(BaseModel):
    name: str
    description: str = Field(max_length=255)

class SourceUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str] = Field(max_length=255)

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

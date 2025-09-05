from typing import Optional

from pydantic import BaseModel
from .core.enums import CategoryType

# Category Schemas
class CategoryCreate(BaseModel):
    name: str
    type: CategoryType

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[CategoryType] = None

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

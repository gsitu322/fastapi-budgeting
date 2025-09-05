from pydantic import BaseModel
from .core.enums import CategoryType


class CreateCategory(BaseModel):
    name: str
    type: CategoryType

class CreateUser(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

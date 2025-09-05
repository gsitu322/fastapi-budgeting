from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.schemas import UserCreate
from app.services.CreateUserService import CreateUserService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("", status_code=status.HTTP_200_OK)
async def get_user():
    pass

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_user(id):
    pass

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user: UserCreate):
    CreateUserService(db).create(user)

@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user):
    pass

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id):
    pass

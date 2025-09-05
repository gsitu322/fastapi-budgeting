from typing import Annotated
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from app.schemas import CreateCategory
from ..services.CreateCategoryService import CreateCategoryService

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_categories():
    pass


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_category(id: int):
    pass


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category: CreateCategory):
    CreateCategoryService(db).create_category(category)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_category(id: int, category):
    pass


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int):
    pass

from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import CategoryCreate, CategoryUpdate
from app.models import Category
from app.services.CreateCategoryService import CreateCategoryService

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

db_dependency = Annotated[Session, Depends(get_db)]

def get_category(db: db_dependency, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

@router.get("", status_code=status.HTTP_200_OK)
async def get_categories(db: db_dependency):
    return db.query(Category).filter(Category.user_id == 1).all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_category(db: db_dependency, id: int):
    category = (db.query(Category)
                .filter(Category.user_id == 1)
                .filter(Category.id == id)
                .first())

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_category(db: db_dependency, category: CategoryCreate):
    CreateCategoryService(db).create_category(category)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_category(db: db_dependency, id: int, category_form: CategoryUpdate):
    category = (db.query(Category)
                .filter(Category.user_id == 1)
                .filter(Category.id == id)
                .first())

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    # Update only the fields provided in the form
    for field, value in category_form.model_dump(mode="json", exclude_unset=True).items():
        setattr(category, field, value)

    db.add(category)
    db.commit()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(db: db_dependency, id: int):
    category = (db.query(Category)
                .filter(Category.user_id == 1)
                .filter(Category.id == id)
                .first())

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
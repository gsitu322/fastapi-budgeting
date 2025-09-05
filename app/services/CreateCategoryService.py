from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import Category
from app.schemas import CreateCategory


class CreateCategoryService:
    def __init__(self, db: Session):
        self.db = db

    def __ensure_category_does_not_exist(self, category_name: str):
        ## TODO: Change User ID
        category = (self.db.query(Category).filter(Category.name.ilike(category_name))
                    .filter(Category.user_id == 1).first())

        if category is not None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail=f"Category {category_name} already exists.")

        return self

    def create_category(self, category: CreateCategory):
        self.__ensure_category_does_not_exist(category.name)

        category_model = Category(**category.model_dump())
        category_model.user_id = 1 # TODO: Change User ID

        self.db.add(category_model)
        self.db.commit()

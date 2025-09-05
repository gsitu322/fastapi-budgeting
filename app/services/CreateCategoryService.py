from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryCreate


class CreateCategoryService:
    def __init__(self, db: Session):
        self._db = db

    def _ensure_category_does_not_exist(self, category_name: str):
        ## TODO: Change User ID
        category = (
            self._db.query(Category)
                .filter(Category.name.ilike(category_name))
                .filter(Category.user_id == 1)
                .first()
        )

        if category is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"Category {category_name} already exists.")

        return self

    def create_category(self, category: CategoryCreate) -> Category:
        self._ensure_category_does_not_exist(category.name)

        category_model = Category(**category.model_dump())
        category_model.user_id = 1 # TODO: Change User ID

        try:
            self._db.add(category_model)
            self._db.commit()
            self._db.refresh(category_model)
        except Exception:
            self._db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create category."
            )

        return category_model

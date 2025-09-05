from fastapi import APIRouter, status
from ..models import Category

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_categories():
    pass

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_category(id: int):
    pass

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_category(category):
    pass

@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_category(id: int, category):
    pass

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int):
    pass


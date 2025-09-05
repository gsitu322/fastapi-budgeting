from fastapi import APIRouter, status
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user():
    pass

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_user(id):
    pass

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(user):
    pass

@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user):
    pass

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id):
    pass

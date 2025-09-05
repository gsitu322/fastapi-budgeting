from fastapi import APIRouter, status
from ..models import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_transactions(id: int):
    pass

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_transaction(id: int):
    pass

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction):
    pass

@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_transaction(id: int, transaction):
    pass

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(id: int):
    pass

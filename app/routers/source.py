from fastapi import APIRouter, status
from pip._internal.index import sources

from ..models import Source

router = APIRouter(
    prefix="/sources",
    tags=["sources"]
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_sources():
    pass

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_source(id: int):
    pass

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_source(source):
    pass


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_source(id: int, source):
    pass


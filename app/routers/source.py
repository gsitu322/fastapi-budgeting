from fastapi import APIRouter, status
from ..models import Source

router = APIRouter(
    prefix="/sources",
    tags=["sources"]
)

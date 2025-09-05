from fastapi import APIRouter, status
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

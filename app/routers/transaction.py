from fastapi import APIRouter, status
from ..models import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

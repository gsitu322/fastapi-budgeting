from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Source
from app.schemas import SourceCreate, SourceUpdate

router = APIRouter(
    prefix="/sources",
    tags=["sources"]
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("", status_code=status.HTTP_200_OK)
async def get_sources(db: db_dependency):
    return db.query(Source).filter(Source.user_id == 1).all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_source(db: db_dependency, id: int):
    return (db.query(Source)
            .filter(Source.id == id)
            .filter(Source.user_id == 1)
            .first())


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_source(db: db_dependency, source: SourceCreate):
    source_model = Source(**source.model_dump())
    source_model.user_id = 1 # TODO: Change User id

    db.add(source_model)
    db.commit()


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_source(db: db_dependency, id: int, source_in: SourceUpdate):
    source = (db.query(Source)
              .filter(Source.id == id)
              .filter(Source.user_id == 1)
              .first())

    for key, value in source_in.model_dump(mode="json", exclude_unset=True).items():
        setattr(source, key, value)

    db.add(source)
    db.commit()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_source(db: db_dependency, id: int):
    source = (db.query(Source)
              .filter(Source.id == id)
              .filter(Source.user_id == 1)
              .first())

    if source is None:
        raise HTTPException(status_code=404, detail="Source not found")

    db.delete(source)
    db.commit()


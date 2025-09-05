from ..models import Category
from sqlalchemy.orm import Session

def get_category(db: Session, id: int):
    return db.query(Category).filter(Category.id == id).first()

def get_categories(db: Session):
    return db.query(Category).all()

def create_category(db: Session, category):
    db.add(category)
    db.commit()
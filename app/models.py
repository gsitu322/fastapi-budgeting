from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, Enum
from .database import Base
from .core.enums import CategoryType


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean)
    create_dt = Column(DateTime, default=datetime.utcnow)
    update_dt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    create_dt = Column(DateTime, default=datetime.utcnow)
    update_dt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(Enum(CategoryType), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    create_dt = Column(DateTime, default=datetime.utcnow)
    update_dt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    notes = Column(String)
    create_dt = Column(DateTime, default=datetime.utcnow)
    update_dt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

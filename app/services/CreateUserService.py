from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import CreateUser
from passlib.context import CryptContext

class CreateUserService:
    def __init__(self, db: Session):
        self._db = db
        self._bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _ensure_user_does_not_exist(self, email: str):
        user = self._db.query(User).filter(func.lower(User.email) == email.lower()).first()

        if user is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Failed to create user", )

        return self

    def create(self, user: CreateUser):
        self._ensure_user_does_not_exist(user.email)

        user_model = User(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=self._bcrypt_context.hash(user.password),
            is_active=True,
        )
        self._db.add(user_model)
        self._db.commit()

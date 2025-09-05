from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import category, source, transaction, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Finance Tracker API is running 🚀"}


app.include_router(category.router)
app.include_router(source.router)
app.include_router(transaction.router)
app.include_router(user.router)

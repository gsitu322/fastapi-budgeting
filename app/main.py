from fastapi import FastAPI
from .routers import category, source, transaction, user

app = FastAPI()

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Finance Tracker API is running 🚀"}


app.include_router(category.router)
app.include_router(source.router)
app.include_router(transaction.router)
app.include_router(user.router)

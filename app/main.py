from fastapi import FastAPI

app = FastAPI()

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Finance Tracker API is running 🚀"}
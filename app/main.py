
from fastapi import FastAPI

app = FastAPI(
    title="CaseZero API",
    description="Backend API for the CaseZero AI Mystery Game",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CaseZero API!",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

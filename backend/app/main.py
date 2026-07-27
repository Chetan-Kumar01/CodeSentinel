from fastapi import FastAPI
from app.routers.upload import router as upload_router

app = FastAPI(
    title="CodeSentinel API",
    version="1.0.0"
)

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message":"Welcome to CodeSentinel 🚀"
    }

@app.get("/health")
def health():
    return {
        "status":"running"
    }
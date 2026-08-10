from fastapi import FastAPI

from app.database import Base, engine
from app import models

from app.routes import auth, tasks


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Secure Task Management API",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Secure Task Management API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routes import auth, tasks

from prometheus_fastapi_instrumentator import Instrumentator


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Secure Task Management API",
    version="1.0.0"
)


# Prometheus metrics
Instrumentator().instrument(app).expose(app)


# Routers
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
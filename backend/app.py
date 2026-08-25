"""
Sales Behavior Intelligence - Main FastAPI Application
This module initializes the FastAPI application, configures CORS,
and includes all the necessary API routers.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.settings import settings
from backend.database.session import Base, engine
from backend.routes import auth, deals, reps, activities, analytics

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(deals.router, prefix="/api/deals", tags=["deals"])
app.include_router(reps.router, prefix="/api/reps", tags=["reps"])
app.include_router(activities.router, prefix="/api/activities", tags=["activities"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

from sqlalchemy import text

@app.get("/health")
def health_check() -> dict:
def health_check():
    db_status = "ok"
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        db_status = "error"
    return {"status": "ok", "app": settings.APP_NAME, "database": db_status}
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok", "app": settings.APP_NAME}

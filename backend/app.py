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

@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}

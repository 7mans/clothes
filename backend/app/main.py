from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import api_router
from .database import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fashion AI Analysis API",
    description="API for analyzing fashion images and providing recommendations.",
    version="1.0.0"
)

# CORS (Cross-Origin Resource Sharing) Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend's domain
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Include the main API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Root"], summary="API Root")
def read_root():
    """
    A simple welcome message to verify the API is running.
    """
    return {"message": "Welcome to the Fashion AI Analysis API"}


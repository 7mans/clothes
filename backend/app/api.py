from fastapi import APIRouter
from .endpoints import analysis

api_router = APIRouter()

# Include the analysis router
api_router.include_router(analysis.router, prefix="/analysis", tags=["Analysis"])


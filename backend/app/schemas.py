from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Base model for Analysis, containing common fields
class AnalysisBase(BaseModel):
    filename: str
    image_url: str
    overview: Optional[str] = None
    clothing_items: Optional[str] = None
    style_analysis: Optional[str] = None
    styling_tips: Optional[str] = None
    occasions: Optional[str] = None

# Schema for creating a new analysis (used in request body)
class AnalysisCreate(AnalysisBase):
    pass

# Schema for reading an analysis (used in response body)
class Analysis(AnalysisBase):
    id: str
    created_at: datetime

    class Config:
        orm_mode = True

# Schema for the recommendation request
class RecommendationRequest(BaseModel):
    analysis_data: Analysis

# Schema for a single outfit recommendation
class OutfitRecommendation(BaseModel):
    occasion: str
    outfit: str
    accessories: str
    tips: str

# Schema for the recommendation response
class RecommendationResponse(BaseModel):
    recommendations: List[OutfitRecommendation]


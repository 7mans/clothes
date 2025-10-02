import shutil
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db
from ..services.vision_service import analyze_image_with_vision_model
from ..services.recommendation_service import generate_recommendations_with_ai

router = APIRouter()

@router.post("/", response_model=schemas.Analysis)
def create_analysis(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Upload an image, save it, and perform an initial analysis.
    """
    # Save the uploaded file to a temporary location
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # For simplicity, we'll use the local file path as the image_url
    # In a real application, you would upload this to a cloud storage service (e.g., S3)
    # and get a public URL.
    image_url = file_path

    # Analyze the image using the vision model
    try:
        analysis_results = analyze_image_with_vision_model(image_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to analyze image: {str(e)}")

    # Create the analysis record in the database
    analysis_data = schemas.AnalysisCreate(
        filename=file.filename,
        image_url=image_url,
        **analysis_results
    )
    return crud.create_analysis(db=db, analysis=analysis_data)

@router.get("/history", response_model=List[schemas.Analysis])
def read_analyses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all analysis records.
    """
    analyses = crud.get_analyses(db, skip=skip, limit=limit)
    return analyses

@router.get("/{analysis_id}", response_model=schemas.Analysis)
def read_analysis(analysis_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a single analysis record by its ID.
    """
    db_analysis = crud.get_analysis(db, analysis_id=analysis_id)
    if db_analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return db_analysis

@router.post("/recommendations", response_model=schemas.RecommendationResponse)
def get_recommendations(request: schemas.RecommendationRequest):
    """
    Generate outfit recommendations based on the provided analysis data.
    """
    try:
        recommendations = generate_recommendations_with_ai(request.analysis_data)
        return schemas.RecommendationResponse(recommendations=recommendations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate recommendations: {str(e)}")


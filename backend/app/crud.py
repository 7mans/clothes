from sqlalchemy.orm import Session
from . import models, schemas

def get_analysis(db: Session, analysis_id: str):
    return db.query(models.Analysis).filter(models.Analysis.id == analysis_id).first()

def get_analyses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Analysis).offset(skip).limit(limit).all()

def create_analysis(db: Session, analysis: schemas.AnalysisCreate):
    db_analysis = models.Analysis(**analysis.dict())
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis


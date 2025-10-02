import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, index=True)
    image_url = Column(String)
    overview = Column(Text, nullable=True)
    clothing_items = Column(Text, nullable=True)
    style_analysis = Column(Text, nullable=True)
    styling_tips = Column(Text, nullable=True)
    occasions = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


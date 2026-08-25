"""
Activity model for tracking sales activities.
"""
from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class Activity(Base):
    """Activity model for tracking sales activities."""
    
    __tablename__ = "activities"
    
    id = Column(String, primary_key=True, index=True)
    deal_id = Column(String, ForeignKey("deals.id"), nullable=False, index=True)
    activity_type = Column(String, nullable=False, index=True)
    description = Column(Text)
    activity_metadata = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    deal = relationship("Deal", back_populates="activities")

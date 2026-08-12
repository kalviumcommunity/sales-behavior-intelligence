"""
Sales representative model.
"""
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class Rep(Base):
    """Sales representative model."""
    
    __tablename__ = "reps"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    role = Column(String, nullable=False)
    deals_count = Column(Integer, default=0)
    quota_attainment = Column(Integer, default=0)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="reps")
    deals = relationship("Deal", back_populates="rep")

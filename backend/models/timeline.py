"""
Timeline event model for deal activity timeline.
"""
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class TimelineEvent(Base):
    """Timeline event model for deal activity timeline."""
    
    __tablename__ = "timeline_events"
    
    id = Column(String, primary_key=True, index=True)
    deal_id = Column(String, ForeignKey("deals.id"), nullable=False, index=True)
    date = Column(String, nullable=False)
    event_type = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    details = Column(Text)
    icon = Column(String, default="📌")
    flag = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    deal = relationship("Deal", back_populates="timeline_events")
    
    # Indexes for common queries
    __table_args__ = (
        Index('idx_timeline_deal_date', 'deal_id', 'date'),
    )

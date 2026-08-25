"""
Deal model for opportunities.
"""

from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class Deal(Base):
    """Deal/opportunity model."""

    __tablename__ = "deals"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    company = Column(String, nullable=False, index=True)
    amount = Column(Float, nullable=False)
    stage = Column(String, nullable=False, index=True)
    rep_id = Column(String, ForeignKey("reps.id"), nullable=False, index=True)
    risk_level = Column(String, nullable=False, index=True)
    risk_score = Column(Integer, nullable=False)
    days_in_stage = Column(Integer, default=0)
    last_activity = Column(String)
    top_flag = Column(String)
    primary_contact = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    rep = relationship("Rep", back_populates="deals")
    activities = relationship(
        "Activity", back_populates="deal", cascade="all, delete-orphan"
    )
    timeline_events = relationship(
        "TimelineEvent", back_populates="deal", cascade="all, delete-orphan"
    )
    coaching_cards = relationship(
        "CoachingCard", back_populates="deal", cascade="all, delete-orphan"
    )

    # Indexes for common queries
    __table_args__ = (
        Index("idx_deal_rep_risk", "rep_id", "risk_level"),
        Index("idx_deal_stage", "stage"),
    )

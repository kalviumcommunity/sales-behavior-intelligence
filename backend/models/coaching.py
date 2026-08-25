"""
Coaching card model for behavioral recommendations.
"""

from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base


class CoachingCard(Base):
    """Coaching card model for behavioral recommendations."""

    __tablename__ = "coaching_cards"

    id = Column(String, primary_key=True, index=True)
    deal_id = Column(String, ForeignKey("deals.id"), nullable=False, index=True)
    flag_title = Column(String, nullable=False)
    severity = Column(String, nullable=False, index=True)
    evidence = Column(Text, nullable=False)
    impact = Column(Text, nullable=False)
    action = Column(Text, nullable=False)
    status = Column(String, default="Needs Coaching", index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    deal = relationship("Deal", back_populates="coaching_cards")

    # Indexes for common queries
    __table_args__ = (
        Index("idx_coaching_deal_severity", "deal_id", "severity"),
        Index("idx_coaching_status", "status"),
    )

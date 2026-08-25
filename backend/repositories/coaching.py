"""
Coaching repository for data access operations.
"""
from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from backend.models.coaching import CoachingCard
from backend.repositories.base import BaseRepository


class CoachingRepository(BaseRepository[CoachingCard]):
    """Repository for CoachingCard model operations."""

    def __init__(self, db: Session):
        super().__init__(CoachingCard, db)

    def get_by_deal_id(self, deal_id: str) -> List[CoachingCard]:
        """Get coaching cards for a deal."""
        return (
            self.db.query(CoachingCard)
            .filter(CoachingCard.deal_id == deal_id)
            .order_by(CoachingCard.created_at)
            .all()
        )

    def get_by_severity(self, severity: str) -> List[CoachingCard]:
        """Get coaching cards by severity."""
        return self.db.query(CoachingCard).filter(CoachingCard.severity == severity).all()

    def get_by_status(self, status: str) -> List[CoachingCard]:
        """Get coaching cards by status."""
        return self.db.query(CoachingCard).filter(CoachingCard.status == status).all()

    def get_by_deal_and_severity(self, deal_id: str, severity: str) -> List[CoachingCard]:
        """Get coaching cards for a deal by severity."""
        return self.db.query(CoachingCard).filter(
            and_(CoachingCard.deal_id == deal_id, CoachingCard.severity == severity)
        ).all()

    def get_high_risk_cards(self) -> List[CoachingCard]:
        """Get high risk coaching cards."""
        return self.get_by_severity("High Risk")

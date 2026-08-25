"""
Deal repository for data access operations.
"""
from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from backend.models.deal import Deal
from backend.repositories.base import BaseRepository


class DealRepository(BaseRepository[Deal]):
    """Repository for Deal model operations."""

    def __init__(self, db: Session):
        super().__init__(Deal, db)

    def get_by_rep_id(self, rep_id: str) -> List[Deal]:
        """Get all deals for a rep."""
        return self.db.query(Deal).filter(Deal.rep_id == rep_id).all()

    def get_by_risk_level(self, risk_level: str) -> List[Deal]:
        """Get deals by risk level."""
        return self.db.query(Deal).filter(Deal.risk_level == risk_level).all()

    def get_by_stage(self, stage: str) -> List[Deal]:
        """Get deals by stage."""
        return self.db.query(Deal).filter(Deal.stage == stage).all()

    def search(self, query: str) -> List[Deal]:
        """Search deals by name or company."""
        like_query = f"%{query}%"
        return self.db.query(Deal).filter(
            or_(Deal.name.ilike(like_query), Deal.company.ilike(like_query))
        ).all()

    def get_with_rep(self, deal_id: str) -> Optional[Deal]:
        """Get deal by ID."""
        return self.get(deal_id)

    def get_high_risk_deals(self) -> List[Deal]:
        """Get high risk deals."""
        return self.get_by_risk_level("High")

    def get_pipeline_value(self) -> float:
        """Get total pipeline value."""
        return sum(deal.amount for deal in self.db.query(Deal).all())

"""
Rep repository for data access operations.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from backend.models.rep import Rep
from backend.repositories.base import BaseRepository


class RepRepository(BaseRepository[Rep]):
    """Repository for Rep model operations."""

    def __init__(self, db: Session):
        super().__init__(Rep, db)

    def get_by_name(self, name: str) -> Optional[Rep]:
        """Get rep by name."""
        return self.db.query(Rep).filter(Rep.name == name).first()

    def get_by_user_id(self, user_id: str) -> Optional[Rep]:
        """Get rep by user ID."""
        return self.db.query(Rep).filter(Rep.user_id == user_id).first()

    def get_with_deals(self, rep_id: str) -> Optional[Rep]:
        """Get rep with their deals."""
        return self.get(rep_id)

    def get_all_with_deals_count(self) -> List[Rep]:
        """Get all reps with deal counts."""
        return self.db.query(Rep).all()

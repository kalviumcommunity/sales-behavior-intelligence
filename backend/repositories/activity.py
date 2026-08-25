"""
Activity repository for data access operations.
"""
from typing import List

from sqlalchemy.orm import Session

from backend.models.activity import Activity
from backend.repositories.base import BaseRepository


class ActivityRepository(BaseRepository[Activity]):
    """Repository for Activity model operations."""

    def __init__(self, db: Session):
        super().__init__(Activity, db)

    def get_by_deal_id(self, deal_id: str) -> List[Activity]:
        """Get activities for a deal."""
        return self.db.query(Activity).filter(Activity.deal_id == deal_id).all()

    def get_by_type(self, activity_type: str) -> List[Activity]:
        """Get activities by type."""
        return self.db.query(Activity).filter(Activity.activity_type == activity_type).all()

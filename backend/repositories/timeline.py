"""
Timeline repository for data access operations.
"""
from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from backend.models.timeline import TimelineEvent
from backend.repositories.base import BaseRepository


class TimelineRepository(BaseRepository[TimelineEvent]):
    """Repository for TimelineEvent model operations."""

    def __init__(self, db: Session):
        super().__init__(TimelineEvent, db)

    def get_by_deal_id(self, deal_id: str) -> List[TimelineEvent]:
        """Get timeline events for a deal ordered by date."""
        return (
            self.db.query(TimelineEvent)
            .filter(TimelineEvent.deal_id == deal_id)
            .order_by(TimelineEvent.date)
            .all()
        )

    def get_by_type(self, event_type: str) -> List[TimelineEvent]:
        """Get events by type."""
        return self.db.query(TimelineEvent).filter(TimelineEvent.event_type == event_type).all()

    def get_with_flag(self, deal_id: str) -> List[TimelineEvent]:
        """Get flagged events for a deal."""
        return (
            self.db.query(TimelineEvent)
            .filter(and_(TimelineEvent.deal_id == deal_id, TimelineEvent.flag.isnot(None)))
            .order_by(TimelineEvent.date)
            .all()
        )

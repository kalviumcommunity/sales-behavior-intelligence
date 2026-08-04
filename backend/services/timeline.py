"""
Timeline service for business logic.
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from backend.schemas.timeline import TimelineEventCreate, TimelineEventUpdate, TimelineListResponse, TimelineEventResponse
from backend.repositories.timeline import TimelineRepository
from backend.repositories.deal import DealRepository
from backend.models.timeline import TimelineEvent


class TimelineService:
    """Service for TimelineEvent business logic."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = TimelineRepository(db)
        self.deal_repository = DealRepository(db)
    
    def create_timeline_event(self, event_in: TimelineEventCreate) -> Optional[TimelineEvent]:
        """Create a new timeline event with validation."""
        # Validate deal exists
        deal = self.deal_repository.get(event_in.deal_id)
        if not deal:
            raise ValueError("Deal not found")
        
        event_data = event_in.model_dump()
        return self.repository.create(event_data)
    
    def get_timeline_event(self, event_id: str) -> Optional[TimelineEvent]:
        """Get timeline event by ID."""
        return self.repository.get(event_id)
    
    def update_timeline_event(self, event_id: str, event_in: TimelineEventUpdate) -> Optional[TimelineEvent]:
        """Update timeline event."""
        event = self.repository.get(event_id)
        if not event:
            return None
        
        update_data = event_in.model_dump(exclude_unset=True)
        return self.repository.update(event, update_data)
    
    def delete_timeline_event(self, event_id: str) -> bool:
        """Delete timeline event."""
        return self.repository.delete(event_id) is not None
    
    def get_timeline_by_deal(self, deal_id: str) -> TimelineListResponse:
        """Get all timeline events for a specific deal."""
        events = self.repository.get_by_deal_id(deal_id)
        event_responses = [TimelineEventResponse.model_validate(event) for event in events]
        return TimelineListResponse(
            events=event_responses,
            total=len(events)
        )
    
    def get_timeline_with_flags(self, deal_id: str) -> List[TimelineEvent]:
        """Get timeline events with flags for a specific deal."""
        return self.repository.get_with_flag(deal_id)

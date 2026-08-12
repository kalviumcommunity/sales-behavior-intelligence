"""
Activity service for business logic.
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from backend.schemas.activity import ActivityCreate, ActivityUpdate
from backend.repositories.activity import ActivityRepository
from backend.repositories.deal import DealRepository
from backend.models.activity import Activity


class ActivityService:
    """Service for Activity business logic."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = ActivityRepository(db)
        self.deal_repository = DealRepository(db)
    
    def create_activity(self, activity_in: ActivityCreate) -> Optional[Activity]:
        """Create a new activity with validation."""
        # Validate deal exists
        deal = self.deal_repository.get(activity_in.deal_id)
        if not deal:
            raise ValueError("Deal not found")
        
        activity_data = activity_in.model_dump()
        return self.repository.create(activity_data)
    
    def get_activity(self, activity_id: str) -> Optional[Activity]:
        """Get activity by ID."""
        return self.repository.get(activity_id)
    
    def update_activity(self, activity_id: str, activity_in: ActivityUpdate) -> Optional[Activity]:
        """Update activity."""
        activity = self.repository.get(activity_id)
        if not activity:
            return None
        
        update_data = activity_in.model_dump(exclude_unset=True)
        return self.repository.update(activity, update_data)
    
    def delete_activity(self, activity_id: str) -> bool:
        """Delete activity."""
        return self.repository.delete(activity_id) is not None
    
    def list_activities(self, skip: int = 0, limit: int = 100) -> List[Activity]:
        """List activities with pagination."""
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def get_activities_by_deal(self, deal_id: str) -> List[Activity]:
        """Get all activities for a specific deal."""
        return self.repository.get_by_deal_id(deal_id)
    
    def get_activities_by_type(self, activity_type: str) -> List[Activity]:
        """Get activities by type."""
        return self.repository.get_by_type(activity_type)

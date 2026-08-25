"""
Rep service for business logic.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from backend.models.rep import Rep
from backend.repositories.rep import RepRepository
from backend.schemas.rep import RepCreate, RepUpdate


class RepService:
    """Service for Rep business logic."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = RepRepository(db)
    
    def create_rep(self, rep_in: RepCreate) -> Rep:
        """Create a new rep."""
        rep_data = rep_in.model_dump()
        return self.repository.create(rep_data)
    
    def get_rep(self, rep_id: str) -> Optional[Rep]:
        """Get rep by ID."""
        return self.repository.get(rep_id)
    
    def get_rep_by_name(self, name: str) -> Optional[Rep]:
        """Get rep by name."""
        return self.repository.get_by_name(name)
    
    def update_rep(self, rep_id: str, rep_in: RepUpdate) -> Optional[Rep]:
        """Update rep."""
        rep = self.repository.get(rep_id)
        if not rep:
            return None
        
        update_data = rep_in.model_dump(exclude_unset=True)
        return self.repository.update(rep, update_data)
    
    def delete_rep(self, rep_id: str) -> bool:
        """Delete rep."""
        return self.repository.delete(rep_id) is not None
    
    def list_reps(self, skip: int = 0, limit: int = 100) -> List[Rep]:
        """List reps with pagination."""
        return self.repository.get_multi(skip=skip, limit=limit)
    
    def get_rep_with_deals(self, rep_id: str) -> Optional[Rep]:
        """Get rep with their deals."""
        return self.repository.get_with_deals(rep_id)
    
    def update_deals_count(self, rep_id: str, count: int) -> Optional[Rep]:
        """Update rep's deals count."""
        rep = self.repository.get(rep_id)
        if not rep:
            return None
        
        return self.repository.update(rep, {"deals_count": count})

"""
Deal service for business logic.
"""
from typing import List, Optional

from sqlalchemy.orm import Session

from backend.models.deal import Deal
from backend.repositories.deal import DealRepository
from backend.repositories.rep import RepRepository
from backend.schemas.deal import (DealCreate, DealListResponse, DealResponse,
                                  DealUpdate)


class DealService:
    """Service for Deal business logic."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = DealRepository(db)
        self.rep_repository = RepRepository(db)
    
    def create_deal(self, deal_in: DealCreate) -> Optional[Deal]:
        """Create a new deal with validation."""
        # Validate rep exists
        rep = self.rep_repository.get(deal_in.rep_id)
        if not rep:
            raise ValueError("Sales representative not found")
        
        deal_data = deal_in.model_dump()
        deal = self.repository.create(deal_data)
        
        # Update rep's deals count
        rep_deals = self.repository.get_by_rep_id(deal_in.rep_id)
        self.rep_repository.update(deal_in.rep_id, {"deals_count": len(rep_deals)})
        
        return deal
    
    def get_deal(self, deal_id: str) -> Optional[Deal]:
        """Get deal by ID with rep information."""
        return self.repository.get_with_rep(deal_id)
    
    def update_deal(self, deal_id: str, deal_in: DealUpdate) -> Optional[Deal]:
        """Update deal with validation."""
        deal = self.repository.get(deal_id)
        if not deal:
            return None
        
        update_data = deal_in.model_dump(exclude_unset=True)
        
        # Validate rep if being updated
        if "rep_id" in update_data:
            rep = self.rep_repository.get(update_data["rep_id"])
            if not rep:
                raise ValueError("Sales representative not found")
        
        return self.repository.update(deal, update_data)
    
    def delete_deal(self, deal_id: str) -> bool:
        """Delete deal and update rep's deals count."""
        deal = self.repository.get(deal_id)
        if not deal:
            return False
        
        rep_id = deal.rep_id
        result = self.repository.delete(deal_id)
        
        # Update rep's deals count
        if result:
            rep_deals = self.repository.get_by_rep_id(rep_id)
            self.rep_repository.update(rep_id, {"deals_count": len(rep_deals)})
        
        return result is not None
    
    def list_deals(
        self, 
        skip: int = 0, 
        limit: int = 100,
        rep_id: Optional[str] = None,
        risk_level: Optional[str] = None,
        stage: Optional[str] = None,
        search: Optional[str] = None
    ) -> DealListResponse:
        """List deals with filters and pagination."""
        filters = {}
        if rep_id:
            filters["rep_id"] = rep_id
        if risk_level:
            filters["risk_level"] = risk_level
        if stage:
            filters["stage"] = stage
        
        if search:
            deals = self.repository.search(search)
            # Apply additional filters to search results
            if filters:
                filtered_deals = []
                for deal in deals:
                    match = True
                    for key, value in filters.items():
                        if getattr(deal, key) != value:
                            match = False
                            break
                    if match:
                        filtered_deals.append(deal)
                deals = filtered_deals
            total = len(deals)
            deals = deals[skip:skip + limit]
        else:
            deals = self.repository.get_multi(skip=skip, limit=limit, filters=filters)
            total = self.repository.count(filters=filters)
        
        # Add rep names to deals
        deal_responses = []
        for deal in deals:
            rep = self.rep_repository.get(deal.rep_id)
            deal_dict = {
                "id": deal.id,
                "name": deal.name,
                "company": deal.company,
                "amount": deal.amount,
                "stage": deal.stage,
                "rep_id": deal.rep_id,
                "rep_name": rep.name if rep else None,
                "risk_level": deal.risk_level,
                "risk_score": deal.risk_score,
                "days_in_stage": deal.days_in_stage,
                "last_activity": deal.last_activity,
                "top_flag": deal.top_flag,
                "primary_contact": deal.primary_contact,
                "created_at": deal.created_at,
                "updated_at": deal.updated_at
            }
            deal_responses.append(DealResponse(**deal_dict))
        
        return DealListResponse(
            deals=deal_responses,
            total=total,
            page=skip // limit + 1,
            page_size=limit
        )
    
    def get_high_risk_deals(self) -> List[Deal]:
        """Get all high risk deals."""
        return self.repository.get_high_risk_deals()
    
    def get_pipeline_value(self) -> float:
        """Get total pipeline value."""
        return self.repository.get_pipeline_value()
    
    def get_deals_by_rep(self, rep_id: str) -> List[Deal]:
        """Get all deals for a specific rep."""
        return self.repository.get_by_rep_id(rep_id)

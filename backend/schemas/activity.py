"""
Pydantic schemas for Activity model.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ActivityBase(BaseModel):
    """Base activity schema."""
    deal_id: str = Field(..., min_length=1)
    activity_type: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = None
    activity_metadata: Optional[str] = None


class ActivityCreate(ActivityBase):
    """Schema for activity creation."""
    pass


class ActivityUpdate(BaseModel):
    """Schema for activity update."""
    activity_type: Optional[str] = None
    description: Optional[str] = None
    activity_metadata: Optional[str] = None


class ActivityResponse(ActivityBase):
    """Schema for activity response."""
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True

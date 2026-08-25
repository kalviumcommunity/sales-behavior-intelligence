"""
Pydantic schemas for CoachingCard model.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CoachingCardBase(BaseModel):
    """Base coaching card schema."""

    deal_id: str = Field(..., min_length=1)
    flag_title: str = Field(..., min_length=1, max_length=200)
    severity: str = Field(..., min_length=1, max_length=20)
    evidence: str = Field(..., min_length=1)
    impact: str = Field(..., min_length=1)
    action: str = Field(..., min_length=1)
    status: str = "Needs Coaching"


class CoachingCardCreate(CoachingCardBase):
    """Schema for coaching card creation."""

    pass


class CoachingCardUpdate(BaseModel):
    """Schema for coaching card update."""

    flag_title: Optional[str] = None
    severity: Optional[str] = None
    evidence: Optional[str] = None
    impact: Optional[str] = None
    action: Optional[str] = None
    status: Optional[str] = None


class CoachingCardResponse(CoachingCardBase):
    """Schema for coaching card response."""

    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CoachingListResponse(BaseModel):
    """Schema for coaching cards list response."""

    cards: list[CoachingCardResponse]
    total: int

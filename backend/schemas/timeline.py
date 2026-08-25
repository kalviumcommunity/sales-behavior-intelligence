"""
Pydantic schemas for TimelineEvent model.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TimelineEventBase(BaseModel):
    """Base timeline event schema."""

    deal_id: str = Field(..., min_length=1)
    date: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1, max_length=50)
    title: str = Field(..., min_length=1, max_length=200)
    details: Optional[str] = None
    icon: str = "📌"
    flag: Optional[str] = None


class TimelineEventCreate(TimelineEventBase):
    """Schema for timeline event creation."""

    pass


class TimelineEventUpdate(BaseModel):
    """Schema for timeline event update."""

    date: Optional[str] = None
    event_type: Optional[str] = None
    title: Optional[str] = None
    details: Optional[str] = None
    icon: Optional[str] = None
    flag: Optional[str] = None


class TimelineEventResponse(TimelineEventBase):
    """Schema for timeline event response."""

    id: str
    created_at: datetime

    class Config:
        from_attributes = True


class TimelineListResponse(BaseModel):
    """Schema for timeline list response."""

    events: list[TimelineEventResponse]
    total: int

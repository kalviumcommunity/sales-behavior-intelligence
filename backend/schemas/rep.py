"""
Pydantic schemas for Rep model.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class RepBase(BaseModel):
    """Base rep schema."""

    name: str = Field(..., min_length=1, max_length=100)
    role: str = Field(..., min_length=1, max_length=50)
    deals_count: int = 0
    quota_attainment: int = 0


class RepCreate(RepBase):
    """Schema for rep creation."""

    user_id: Optional[str] = None


class RepUpdate(BaseModel):
    """Schema for rep update."""

    name: Optional[str] = None
    role: Optional[str] = None
    deals_count: Optional[int] = None
    quota_attainment: Optional[int] = None


class RepResponse(RepBase):
    """Schema for rep response."""

    id: str
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

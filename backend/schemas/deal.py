"""
Pydantic schemas for Deal model.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DealBase(BaseModel):
    """Base deal schema."""
    name: str = Field(..., min_length=1, max_length=200)
    company: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    stage: str = Field(..., min_length=1, max_length=50)
    rep_id: str = Field(..., min_length=1)
    risk_level: str = Field(..., min_length=1, max_length=20)
    risk_score: int = Field(..., ge=0, le=100)
    days_in_stage: int = 0
    last_activity: Optional[str] = None
    top_flag: Optional[str] = None
    primary_contact: Optional[str] = None


class DealCreate(DealBase):
    """Schema for deal creation."""
    pass


class DealUpdate(BaseModel):
    """Schema for deal update."""
    name: Optional[str] = None
    company: Optional[str] = None
    amount: Optional[float] = Field(None, gt=0)
    stage: Optional[str] = None
    risk_level: Optional[str] = None
    risk_score: Optional[int] = Field(None, ge=0, le=100)
    days_in_stage: Optional[int] = None
    last_activity: Optional[str] = None
    top_flag: Optional[str] = None
    primary_contact: Optional[str] = None


class DealResponse(DealBase):
    """Schema for deal response."""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class DealListResponse(BaseModel):
    """Schema for deal list response."""
    deals: list[DealResponse]
    total: int
    page: int
    page_size: int

"""
Pydantic schemas for User model.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class UserBase(BaseModel):
    """Base user schema."""
    email: str = Field(..., min_length=5, max_length=100)
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None
    role: str = "rep"
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v


class UserCreate(UserBase):
    """Schema for user creation."""
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Schema for user update."""
    email: Optional[str] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """Schema for user in database."""
    id: str
    hashed_password: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserResponse(UserBase):
    """Schema for user response."""
    id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema for authentication token."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema for token data."""
    username: Optional[str] = None
    role: Optional[str] = None

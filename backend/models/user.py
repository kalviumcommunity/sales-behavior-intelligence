"""
User model for authentication and authorization.
"""
import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database import Base


class UserRole(str, enum.Enum):
    """User roles for authorization."""
    ADMIN = "admin"
    MANAGER = "manager"
    REP = "rep"


class User(Base):
    """User model for authentication."""
    
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.REP, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    reps = relationship("Rep", back_populates="user", uselist=False)

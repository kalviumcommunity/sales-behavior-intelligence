"""
User repository for data access operations.
"""
from typing import Optional

from sqlalchemy.orm import Session

from backend.models.user import User
from backend.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for User model operations."""

    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def email_exists(self, email: str) -> bool:
        """Check if email exists."""
        return self.get_by_email(email) is not None

    def username_exists(self, username: str) -> bool:
        """Check if username exists."""
        return self.get_by_username(username) is not None

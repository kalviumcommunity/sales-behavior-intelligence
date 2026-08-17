"""
User service for business logic.
"""
from typing import Optional
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserUpdate
from backend.repositories.user import UserRepository
from backend.models.user import User
from backend.auth.security import get_password_hash


class UserService:
    """Service for User business logic."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)
    
    def create_user(self, user_in: UserCreate) -> User:
        """Create a new user with validation."""
        if self.repository.email_exists(user_in.email):
            raise ValueError("Email already registered")
        if self.repository.username_exists(user_in.username):
            raise ValueError("Username already taken")
        
        user_data = user_in.model_dump(exclude={"password"})
        user_data["hashed_password"] = get_password_hash(user_in.password)
        return self.repository.create(user_data)
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        return self.repository.get(user_id)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.repository.get_by_email(email)
    
    def update_user(self, user_id: str, user_in: UserUpdate) -> Optional[User]:
        """Update user with validation."""
        user = self.repository.get(user_id)
        if not user:
            return None
        
        update_data = user_in.model_dump(exclude_unset=True)
        
        # Check email uniqueness if being updated
        if "email" in update_data and update_data["email"] != user.email:
            if self.repository.email_exists(update_data["email"]):
                raise ValueError("Email already registered")
        
        return self.repository.update(user, update_data)
    
    def delete_user(self, user_id: str) -> bool:
        """Delete user."""
        return self.repository.delete(user_id) is not None
    
    def list_users(self, skip: int = 0, limit: int = 100):
        """List users with pagination."""
        return self.repository.get_multi(skip=skip, limit=limit)

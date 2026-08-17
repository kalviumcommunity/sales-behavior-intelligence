"""
Authentication service for user registration and login.
"""
from datetime import timedelta
from typing import Optional

from sqlalchemy.orm import Session

from backend.auth.security import create_access_token, get_password_hash, verify_password
from backend.config.settings import settings
from backend.repositories.user import UserRepository
from backend.schemas.user import Token, UserCreate


class AuthService:
    """Service for authentication operations."""

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(self, user_in: UserCreate):
        """Register a new user."""
        if self.user_repository.email_exists(user_in.email):
            raise ValueError("Email already registered")
        if self.user_repository.username_exists(user_in.username):
            raise ValueError("Username already taken")

        user_data = user_in.model_dump(exclude={"password"})
        user_data["hashed_password"] = get_password_hash(user_in.password)
        return self.user_repository.create(user_data)

    def authenticate_user(self, username: str, password: str) -> Optional[object]:
        """Authenticate a username and password."""
        user = self.user_repository.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    def login(self, username: str, password: str) -> Token:
        """Login user and return access token."""
        user = self.authenticate_user(username, password)
        if not user:
            raise ValueError("Incorrect username or password")

        access_token = create_access_token(
            data={"sub": user.username, "role": user.role.value if hasattr(user.role, "value") else user.role},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        return Token(access_token=access_token, token_type="bearer")

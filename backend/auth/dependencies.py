"""
Authentication dependencies for FastAPI routes.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.auth.security import decode_access_token
from backend.database import get_db
from backend.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get the current authenticated user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    username = payload.get("sub") if payload else None
    if username is None:
        raise credentials_exception

    user = UserRepository(db).get_by_username(username)
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return user


async def get_current_active_user(current_user=Depends(get_current_user)):
    """Get the current active user."""
    return current_user


async def get_current_manager(current_user=Depends(get_current_user)):
    """Require manager or admin role."""
    role = current_user.role.value if hasattr(current_user.role, "value") else current_user.role
    if role not in ["admin", "manager"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return current_user


async def get_current_admin(current_user=Depends(get_current_user)):
    """Require admin role."""
    role = current_user.role.value if hasattr(current_user.role, "value") else current_user.role
    if role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return current_user

"""Authentication module."""

from .dependencies import (
    get_current_active_user,
    get_current_admin,
    get_current_manager,
    get_current_user,
    oauth2_scheme,
)
from .security import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password,
)
from .service import AuthService

__all__ = [
    "AuthService",
    "create_access_token",
    "decode_access_token",
    "get_current_active_user",
    "get_current_admin",
    "get_current_manager",
    "get_current_user",
    "get_password_hash",
    "oauth2_scheme",
    "verify_password",
]

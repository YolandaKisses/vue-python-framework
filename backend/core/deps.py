"""Dependency injection for FastAPI."""

from typing import Annotated, Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel

from core.config import settings

# Security scheme
security = HTTPBearer()


class TokenData(BaseModel):
    """Token payload data structure."""
    user_id: str | None = None
    username: str | None = None
    email: str | None = None


def get_db() -> Generator:
    """Database session dependency."""
    # Placeholder for database session
    # In production, use SQLAlchemy async session
    yield None


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> TokenData:
    """Validate JWT token and extract user information."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            credentials.credential,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )
        user_id: str = payload.get("sub")
        username: str = payload.get("username")
        email: str = payload.get("email")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id, username=username, email=email)
    except JWTError:
        raise credentials_exception
    return token_data


# Type aliases for dependency injection
DBSession = Annotated[Generator, Depends(get_db)]
CurrentUser = Annotated[TokenData, Depends(get_current_user)]
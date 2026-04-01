"""Authentication endpoints."""

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.config import settings
from core.deps import TokenData
from schemas import Token, User, UserCreate

router = APIRouter()


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create JWT access token."""
    from jose import jwt
    to_encode = data.copy()
    expire = timedelta(minutes=settings.access_token_expire_minutes)
    if expires_delta:
        expire = expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
    return encoded_jwt


@router.post("/register", response_model=User)
async def register(user_data: UserCreate) -> User:
    """Register a new user."""
    # Placeholder implementation
    # In production, validate and save to database
    return User(
        id=1,
        email=user_data.email,
        username=user_data.username,
        is_active=True,
    )


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """User login and get access token."""
    # Placeholder implementation
    # In production, validate credentials against database
    access_token = create_access_token(
        data={"sub": "1", "email": form_data.username}
    )
    return Token(
        access_token=access_token,
        token_type="bearer",
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(current_user: Annotated[TokenData, Depends()]) -> Token:
    """Refresh access token."""
    # Placeholder implementation
    access_token = create_access_token(
        data={"sub": str(current_user.user_id), "email": current_user.email}
    )
    return Token(
        access_token=access_token,
        token_type="bearer",
    )


@router.post("/logout")
async def logout() -> dict[str, str]:
    """User logout."""
    # Placeholder implementation
    # In production, invalidate token if using blacklist
    return {"message": "Successfully logged out"}
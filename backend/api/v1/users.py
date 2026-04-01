"""User management endpoints."""

from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status

from core.deps import CurrentUser, DBSession
from schemas import User, UserUpdate

router = APIRouter()


@router.get("", response_model=List[User])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    _: DBSession = None,
) -> List[User]:
    """Get list of users."""
    # Placeholder implementation
    return []


@router.get("/me", response_model=User)
async def get_current_user_info(
    current_user: CurrentUser,
) -> User:
    """Get current authenticated user information."""
    # Placeholder implementation
    return User(
        id=current_user.user_id or 0,
        email=current_user.email or "",
        username=current_user.email or "user",
        is_active=True,
    )


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    _: DBSession = None,
) -> User:
    """Get user by ID."""
    # Placeholder implementation
    return User(
        id=user_id,
        email=f"user{user_id}@example.com",
        username=f"user{user_id}",
        is_active=True,
    )


@router.patch("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    _: DBSession = None,
) -> User:
    """Update user information."""
    # Placeholder implementation
    return User(
        id=user_id,
        email=user_update.email or f"user{user_id}@example.com",
        username=user_update.username or f"user{user_id}",
        is_active=user_update.is_active if user_update.is_active is not None else True,
    )


@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    _: DBSession = None,
) -> dict[str, str]:
    """Delete user by ID."""
    # Placeholder implementation
    return {"message": f"User {user_id} deleted"}
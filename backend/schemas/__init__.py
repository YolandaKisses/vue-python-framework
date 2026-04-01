"""Pydantic schemas for request/response validation."""

from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


# Token schemas
class Token(BaseModel):
    """OAuth2 token response schema."""
    access_token: str
    token_type: str = "bearer"


# User schemas
class UserBase(BaseModel):
    """Base user schema with common fields."""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)


class UserCreate(UserBase):
    """Schema for user registration."""
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Schema for user update."""
    email: EmailStr | None = None
    username: str | None = Field(None, min_length=3, max_length=50)
    is_active: bool | None = None


class User(UserBase):
    """User response schema."""
    id: int
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}
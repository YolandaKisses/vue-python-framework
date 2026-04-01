"""API v1 router - aggregates all API routes."""

from fastapi import APIRouter

from api.v1 import health, auth

api_router = APIRouter()

# Include sub-routers
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
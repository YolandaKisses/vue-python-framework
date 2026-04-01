"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check() -> dict[str, str]:
    """Basic health check."""
    return {"status": "ok"}


@router.get("/detailed")
async def detailed_health() -> dict[str, str]:
    """Detailed health check with version info."""
    from core.config import settings
    return {
        "status": "ok",
        "version": settings.app_version,
        "debug": str(settings.debug),
    }
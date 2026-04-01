"""Utilities module - helper functions."""

from datetime import datetime, timezone


def utc_now() -> datetime:
    """Get current UTC datetime."""
    return datetime.now(timezone.utc)


def format_datetime(dt: datetime | None) -> str | None:
    """Format datetime to ISO string."""
    if dt is None:
        return None
    return dt.isoformat()
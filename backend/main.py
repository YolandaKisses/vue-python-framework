"""Main entry point for FastAPI application."""

import uvicorn
from core.config import settings
from core.app import app


if __name__ == "__main__":
    uvicorn.run(
        "core.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )
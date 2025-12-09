from typing import Any
import logging

from sqlalchemy.ext.asyncio import AsyncEngine

from .db import Base

logger = logging.getLogger(__name__)


async def init_db(engine: AsyncEngine) -> None:
    """Create database tables for all declarative models.

    This uses an async engine and runs the synchronous
    Base.metadata.create_all in a thread via ``conn.run_sync``.
    """
    if engine is None:
        logger.warning("No engine provided to init_db; skipping table creation.")
        return

    # Use engine.begin() and run_sync to execute metadata.create_all
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables created (if not present).")
    except Exception as exc:  # pragma: no cover - simple error handling
        logger.exception("Failed to initialize database: %s", exc)
        raise

"""Application lifespan and service router"""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan_service_router(_app: FastAPI) -> AsyncGenerator[None]:
    """Log startup and shutdown of the service router"""
    logger.debug("Lifespan (service router) startup")
    yield
    logger.debug("Lifespan (service router) shutdown")


@asynccontextmanager
async def lifespan_app(_app: FastAPI) -> AsyncGenerator[None]:
    """Log startup and shutdown of the application"""
    logger.debug("Lifespan (app) startup")
    yield
    logger.debug("Lifespan (app) shutdown")

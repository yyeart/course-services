"""Web-application factory"""

from collections.abc import Iterable
from typing import Any

from fastapi import APIRouter, FastAPI

from src.core.config import Settings


def create_app(
    settings: Settings,
    routers: Iterable[APIRouter],
    **params: Any,
) -> FastAPI:
    """Creates app with given parameters and routers"""
    app_params = {**settings.app.model_dump(), **params}
    app = FastAPI(**app_params)
    for router in routers:
        app.include_router(router)
    return app

"""Load and cache application settings from the environment."""

import functools
from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Define application metadata and debug settings."""

    title: str = "Course service title"
    description: str = "Course service description"
    summary: str = "Course service summary"
    version: str = "0.1.0"
    debug: bool = False


@final
class Settings(BaseSettings):
    """Load service configuration from environment variables and .env."""

    app: AppSettings

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )


@functools.lru_cache
def get_settings() -> Settings:
    """Return the cached service settings."""
    return Settings()

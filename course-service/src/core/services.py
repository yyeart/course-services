"""Service status getters"""

from src.web.schemas import ServiceInfo


def get_settings_info() -> ServiceInfo:
    """Returns current service status"""
    return ServiceInfo()

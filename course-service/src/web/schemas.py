"""Define response schemas and model configuration"""

from pydantic import BaseModel, ConfigDict


class BaseSchemaModel(BaseModel):
    """Provide shared validation and attribute-loading settings"""

    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        populate_by_name=True,
    )


class ServiceInfo(BaseSchemaModel):
    """Represent the service health status."""

    healthy: bool = True

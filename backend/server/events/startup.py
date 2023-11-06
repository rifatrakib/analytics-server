from typing import Any, Dict

from fastapi import status

from server.config import settings
from server.models.schemas.responses.misc import AppInformation, MessageResponse


def get_app_information() -> Dict[str, Any]:
    with open("README.md") as reader:
        description = reader.read()

    return AppInformation(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        summary="An innovative approach to a possible substitute for database-driven analytics",
        description=description,
        version=settings.VERSION,
        openapi_url="/openapi.json" if settings.DEBUG else None,
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
    ).model_dump()


def define_responses() -> Dict[int, Dict[str, Any]]:
    options = {"model": MessageResponse, "exclude_unset": True}
    return {
        status.HTTP_400_BAD_REQUEST: options,
        status.HTTP_401_UNAUTHORIZED: options,
        status.HTTP_403_FORBIDDEN: options,
        status.HTTP_404_NOT_FOUND: options,
        status.HTTP_422_UNPROCESSABLE_ENTITY: options,
    }

from typing import List, Union

from server.models.schemas import BaseResponseSchema


class HealthResponse(BaseResponseSchema):
    app_name: str
    mode: str
    debug: bool


class MessageResponse(BaseResponseSchema):
    loc: Union[List[str], None] = None
    msg: str
    type: Union[str, None] = None


class AppInformation(BaseResponseSchema):
    title: str
    debug: bool
    summary: str
    description: str
    version: str
    openapi_url: Union[str, None] = None
    docs_url: Union[str, None] = None
    redoc_url: Union[str, None] = None

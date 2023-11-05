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

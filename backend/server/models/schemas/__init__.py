from typing import Union

from pydantic import ConfigDict, validator

from server.models import BaseSchema


class BaseAPISchema(BaseSchema):
    pass


class BaseRequestSchema(BaseAPISchema):
    model_config = ConfigDict(extra="forbid")


class BaseResponseSchema(BaseAPISchema):
    id: Union[str, None] = None

    @validator("id", pre=True)
    def convert_id(cls, v):
        if v:
            return str(v)

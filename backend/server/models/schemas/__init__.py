from datetime import datetime, timezone
from typing import List, Union

from pydantic import BaseModel, ConfigDict, validator
from pydash import camel_case


class BaseAPISchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=camel_case,
        json_encoders={
            datetime: lambda v: v.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z"),
        },
    )


class BaseRequestSchema(BaseAPISchema):
    model_config = ConfigDict(extra="forbid")


class BaseResponseSchema(BaseAPISchema):
    id: Union[str, None] = None

    @validator("id", pre=True)
    def convert_id(cls, v):
        if v:
            return str(v)


class HealthResponseSchema(BaseAPISchema):
    APP_NAME: str
    MODE: str
    DEBUG: bool


class MessageResponseSchema(BaseResponseSchema):
    loc: Union[List[str], None] = None
    msg: str
    type: Union[str, None] = None

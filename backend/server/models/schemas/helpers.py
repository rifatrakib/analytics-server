from datetime import datetime

from server.models.schemas import BaseSchema


class Activity(BaseSchema):
    place: str
    time: datetime
    battery: int
    temperature: int

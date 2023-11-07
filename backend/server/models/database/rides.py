from datetime import datetime

from server.models.database import BaseDocument
from server.models.schemas import BaseSchema


class Activity(BaseSchema):
    place: str
    time: datetime
    battery: int
    temperature: int


class Ride(BaseDocument):
    account: str
    bike: int
    depart_from: Activity
    return_at: Activity
    formula: str
    stopover_duration: int
    number_of_stopovers: int

from server.models.database import BaseDocument
from server.models.schemas.helpers import Activity


class Ride(BaseDocument):
    account: str
    bike: int
    depart_from: Activity
    return_at: Activity
    formula: str
    stopover_duration: int
    number_of_stopovers: int

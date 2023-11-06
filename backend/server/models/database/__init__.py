from datetime import datetime
from typing import Union

from beanie import Document

from server.models import BaseSchema


class BaseDocument(Document, BaseSchema):
    created_at: datetime = datetime.utcnow()
    last_updated_at: Union[datetime, None] = None

    async def save(self):
        if self.id:
            self.last_updated_at = datetime.utcnow()
        return await super().save()

from fastapi import FastAPI

from server.config import settings
from server.models.schemas import HealthResponseSchema

app = FastAPI()


@app.get("/health", response_model=HealthResponseSchema)
async def health():
    return settings

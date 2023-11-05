from fastapi import FastAPI, status

from server.config import settings
from server.models.schemas.responses.misc import HealthResponse, MessageResponse

app = FastAPI(
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": MessageResponse, "exclude_unset": True},
    },
)


@app.get("/health", response_model=HealthResponse, response_model_exclude_unset=True)
async def health():
    return settings.health_check

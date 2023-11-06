from fastapi import FastAPI

from server.config import settings
from server.events.startup import define_responses, get_app_information
from server.models.schemas.responses.misc import HealthResponse

app = FastAPI(
    **get_app_information(),
    responses=define_responses(),
)


@app.get("/health", response_model=HealthResponse, response_model_exclude_unset=True)
async def health():
    return settings.health_check

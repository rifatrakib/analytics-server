from fastapi import FastAPI

from server.config import settings

app = FastAPI()


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "message": f"{settings.APP_NAME} is running in {settings.MODE} mode",
    }

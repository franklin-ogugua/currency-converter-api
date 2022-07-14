from fastapi import APIRouter, Depends

from converter.config import Settings, get_settings

router = APIRouter()


@router.get("/ping", tags=["status"])
async def check_api_server_status(settings: Settings = Depends(get_settings)):
    """
    Checks API Server Status
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }

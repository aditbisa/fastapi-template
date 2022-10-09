from fastapi import APIRouter, status

from app.database import engine

router = APIRouter(prefix="/healthchecks")


@router.get("/readiness", status_code=status.HTTP_200_OK, tags=["health"])
async def readiness():
    """
    Readiness healthcheck endpoint.
    """

    with engine.connect() as connection:
        connection.execute("SELECT 1")

    return "OK 👍"

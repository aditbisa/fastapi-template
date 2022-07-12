from fastapi import APIRouter, status

router = APIRouter(prefix="/healthchecks")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["health"]
)
async def readiness():
    """
    Readiness healthcheck endpoint.
    """
    return "OK 👍"

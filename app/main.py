from fastapi import FastAPI

from app.routers import healtchecks, playgrounds

app = FastAPI(
    title="Rest API template",
)
app.include_router(healtchecks.router)
app.include_router(playgrounds.router)

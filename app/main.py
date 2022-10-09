from fastapi import FastAPI

from app.middlewares.authentications import AuthMiddleware
from app.routers import authentications, healtchecks, playgrounds

app = FastAPI(
    title="Rest API template",
)
app.add_middleware(
    AuthMiddleware,
    exempt_paths=[
        "/docs",
        "/openapi.json",
        "/redoc",
        "/healthchecks/readiness",
        "/token",
    ],
)
app.include_router(authentications.router)
app.include_router(healtchecks.router)
app.include_router(playgrounds.router)

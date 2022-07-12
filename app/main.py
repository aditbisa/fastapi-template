from a2wsgi import ASGIMiddleware
from fastapi import FastAPI

from .routers import healtchecks


app = FastAPI(
    title="SM API",
)
app.include_router(healtchecks.router)

wsgi_app = ASGIMiddleware(app)

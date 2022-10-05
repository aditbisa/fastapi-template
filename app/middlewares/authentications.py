from typing import List

from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.configs import oauth2_scheme
from app.services.authentications import verify_access_token


class AuthMiddleware(BaseHTTPMiddleware):
    """
    Authenticate token.
    """

    def __init__(self, app, exempt_paths: List[str] = None):
        super().__init__(app)
        self.exempt_paths = exempt_paths if exempt_paths else []

    async def dispatch(self, request: Request, call_next):
        if request.scope["path"] not in self.exempt_paths and request.scope["method"] != "OPTIONS":
            access_token = await oauth2_scheme(request)
            user_id = verify_access_token(access_token)

            if not user_id:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"detail": "Could not validate credentials"},
                    headers={"WWW-Authenticate": "Bearer"},
                )

            # Save user_id in request state
            request.state.user_id = user_id

        response = await call_next(request)
        return response

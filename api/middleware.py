from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from infrastructure.loggers.container import LoggerContainer


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._logger = LoggerContainer()

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        token = request.headers.get("Authorization")
        if token:
            response = await call_next(request)
            return response


class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._logger = LoggerContainer()

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        self._logger.get_logger("INFO").msg(
            f"{request.client.host} {request.method} {request.url} {response.status_code}"
        )
        return response


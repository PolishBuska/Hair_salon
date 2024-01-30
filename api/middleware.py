from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware

from infrastructure.loggers.container import LoggerContainer


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


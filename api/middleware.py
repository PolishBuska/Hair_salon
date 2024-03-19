import json

from fastapi import Request, status
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from infrastructure.loggers.container import LoggerContainer
from infrastructure.adapters.keycloak.admin import container_factory

from application.dto.user import CurrentUserDTO

from config import get_config


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


class MasterAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._openid = container_factory().get_openid
        self._restricted_path = get_config().master_path

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if self._restricted_path in request.url.path:
            if request.cookies.get('access_token'):
                token = request.cookies.get('access_token')
                token = token.replace("'", "\"")
                token_data = json.loads(token)
                access_token = token_data.get('access_token', '')
                raw_user = self._openid.userinfo(access_token)
                current_user = CurrentUserDTO(
                    user_id=raw_user["sub"],
                    role=raw_user["realm_access"]["roles"],
                    email=raw_user["email"],
                    email_verified=raw_user["email_verified"],
                    username=raw_user["preferred_username"]
                )
                if self._restricted_path.capitalize() not in current_user.role:
                    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content="User's not a Master")
                request.state.current_user = current_user
                response = await call_next(request)
                return response
            else:
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Not Authorized")
        else:
            response = await call_next(request)
            return response


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._openid = container_factory().get_openid
        self._restricted_path = get_config().master_path

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if 'me' in request.url.path:
            if request.cookies.get('access_token'):
                token = request.cookies.get('access_token')
                token = token.replace("'", "\"")
                token_data = json.loads(token)
                access_token = token_data.get('access_token', '')

                raw_user = self._openid.userinfo(access_token)
                current_user = CurrentUserDTO(
                    user_id=raw_user["sub"],
                    role=raw_user["realm_access"]["roles"],
                    email=raw_user["email"],
                    email_verified=raw_user["email_verified"],
                    username=raw_user["preferred_username"]
                )

                request.state.current_user = current_user
                response = await call_next(request)
                return response
            else:
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="Not Authorized")
        else:
            response = await call_next(request)
            return response

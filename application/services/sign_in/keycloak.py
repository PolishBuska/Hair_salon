from core.models.user import UserCreds

from infrastructure.adapters.keycloak.admin import AdminContainer

from application.exceptions.services import NoTokenException, KeycloakSignInException

from core.interfaces.services.login import LoginServiceInterface


class LoginService(LoginServiceInterface):
    def __init__(self, admin: AdminContainer):
        self._admin = admin.get_admin
        self._openid = admin.get_openid

    async def login(self, user_creds: UserCreds):
        try:
            token = self._openid.token(username=user_creds.username,
                                       password=user_creds.password)
            if not token:
                raise NoTokenException(
                    f"Wrong Credentials"
                )
            return {"access_token": token['access_token'], "token_type": "bearer"}
        except Exception as e:
            raise KeycloakSignInException(
                f"Sign-in service couldn't get the token. Original error {str(e)}"
                                          ) from e

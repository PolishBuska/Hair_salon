from domain.models.user import User
from keycloak import KeycloakAdmin


class KeycloakGateway:
    def __init__(self, admin: KeycloakAdmin):
        self._admin = admin

    def create_user(self, user_data: User):

        new_user = self._admin.create_user(payload={
            "email": user_data.email,
            "username": user_data.nickname,
            "enabled": True,
            "credentials": [
                {"value": user_data.password, "type": "password"}
            ]
        }, exist_ok=True)
        return new_user


def keycloak_gateway_factory(admin):
    return KeycloakGateway(admin)

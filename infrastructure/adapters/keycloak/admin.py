from keycloak import KeycloakAdmin, KeycloakOpenID

from config import get_config


class AdminContainer:
    def __init__(self):
        self._config = get_config()

        self._server_url = self._config.server_url
        self._username = self._config.username
        self._password = self._config.password
        self._realm_name = self._config.realm_name
        self._client_id = self._config.client_id
        self._client_secret_key = self._config.client_secret_key
        self._keycloak_openid = KeycloakOpenID(
            realm_name=self._realm_name,
            server_url=self._server_url,
            client_id=self._client_id,
            client_secret_key=self._client_secret_key,
            verify=True,
        )
        self._admin = KeycloakAdmin(realm_name=self._realm_name,
                                    username=self._username,
                                    password=self._password,
                                    server_url=self._server_url,
                                    client_id=self._client_id,
                                    client_secret_key=self._client_secret_key,
                                    verify=True
                                    )

    @property
    def get_admin(self) -> KeycloakAdmin:
        return self._admin

    @property
    def get_openid(self) -> KeycloakOpenID:
        return self._keycloak_openid

    @property
    def get_client_id(self) -> str:
        return self._admin.get_client_id(client_id=self._client_id)


def container_factory() -> AdminContainer:
    return AdminContainer()

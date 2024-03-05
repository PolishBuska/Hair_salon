from abc import ABC, abstractmethod

from keycloak import KeycloakOpenID, KeycloakAdmin


class KeycloakAdminContainer(ABC):

    @property
    @abstractmethod
    def get_admin(self) -> KeycloakAdmin:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_openid(self) -> KeycloakOpenID:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_client_id(self) -> str:
        raise NotImplementedError

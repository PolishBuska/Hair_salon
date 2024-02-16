
from domain.interfaces.services.user import UserServiceInterface
from domain.models.user import User

from api.schemas.user import Roles

from infrastructure.adapters.keycloak.admin import AdminContainer
from infrastructure.gateways.keycloak import keycloak_gateway_factory


class UserService(UserServiceInterface):
    def __init__(self, admin: AdminContainer):
        self._admin = admin.get_admin
        self._client_id = admin.get_client_id
        self._gateway = keycloak_gateway_factory(self._admin)

    async def register(self, user_data: User):
        new_user = self._gateway.create_user(user_data)
        customer = self._admin.get_realm_role('Customer')
        master = self._admin.get_realm_role('Master')
        if user_data.role_id == Roles.Master:
            self._admin.assign_realm_roles(user_id=new_user, roles=[master])
        elif user_data.role_id == Roles.Customer:
            self._admin.assign_realm_roles(roles=[customer], user_id=new_user)

        return new_user


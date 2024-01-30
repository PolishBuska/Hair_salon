from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_host: str
    app_port: int
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    model_config = SettingsConfigDict(env_file='.env', extra="allow")

    @property
    def db_url(self):
        url = f'postgresql+asyncpg://{self.database_username}:' \
                                  f'{self.database_password}@' \
                                  f'{self.database_hostname}:' \
                                  f'{self.database_port}/' \
                                  f'{self.database_name}'
        return url

    @property
    def test_db_url(self):
        url = f'postgresql+asyncpg://{self.database_username}:' \
              f'{self.database_password}@' \
              f'{self.database_hostname}:' \
              f'{self.database_port}/' \
              f'{self.database_name}_test'
        return url


def get_config() -> Settings:
    return Settings()

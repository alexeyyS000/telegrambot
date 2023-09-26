from pydantic_settings import BaseSettings, SettingsConfigDict


class AdminSettings(BaseSettings):
    bot_token: str

    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), extra="allow")

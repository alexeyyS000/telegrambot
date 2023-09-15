from pydantic import BaseSettings


class AdminSettings(BaseSettings):
    bot_token: str

    class Config:
        env_file = (".env", ".env.local")

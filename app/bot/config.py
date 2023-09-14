from pydantic import BaseSettings


class AdminSettings(BaseSettings):
    bot_token: str
    admin_id: int

    class Config:
        env_file = (".env", ".env.local")

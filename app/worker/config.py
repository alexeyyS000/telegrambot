from pydantic import BaseSettings


class WorkerSettings(BaseSettings):
    celery_broker_url: str  # = "redis://localhost:6379/0"
    celery_result_backend: str  # = "redis://localhost:6379/1"

    class Config:
        env_file = (".env", ".env.local")

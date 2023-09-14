from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    name: Optional[str]
    admin: bool = False
    subscriber: bool = False
    pending: bool = False
    banned: bool = False

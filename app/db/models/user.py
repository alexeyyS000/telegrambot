from db.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Boolean, BigInteger, String


class User(Base):
    __tablename__ = "users"
    id = mapped_column(BigInteger, primary_key=True)
    name = mapped_column(String, nullable=True, default=None)
    admin = mapped_column(Boolean, nullable=False, default=False)
    subscriber = mapped_column(Boolean, nullable=False, default=False)
    pending = mapped_column(Boolean, nullable=False, default=False)
    banned = mapped_column(Boolean, nullable=False, default=False)

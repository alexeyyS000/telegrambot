from db.dal.user import UserDAL
from db.client import get_session
import contextlib
from exceptions import *


@contextlib.contextmanager
def get_user_service(id):
    with get_session() as session:
        user_dal = UserDAL(session)
        yield UserService(user_dal, id)


class UserService:
    def __init__(self, dal, id):
        self.dal = dal
        self.instance = self.dal.get_one_or_none(id=id)
        if self.instance is None:
            self.id = id

    def ban(self):
        if not self.instance.banned:
            self.dal.update_one(
                {"admin": False, "pending": False, "subscriber": False, "banned": True},
                id=self.instance.id,
            )
        else:
            raise AlreadyBanned("Already added")

    def add(self):
        if not self.instance.subscriber:
            self.dal.update_one(
                {"pending": False, "subscriber": True}, id=self.instance.id
            )
        else:
            raise AlreadyAdded("Already added")

    def make_admin(self):
        if not self.instance.admin:
            self.dal.update_one({"admin": True}, id=self.instance.id)
        else:
            raise AlreadyAdmin("Already admin")

    def refusal(self):
        if self.instance is not None:
            self.dal.delete_one(id=self.instance.id)
        else:
            raise AlreadyRefusaled("Already refusaled")

    def create(self, **kwargs):
        if self.instance is not None:
            raise AlreadyExists("Already exist")
        kwargs["id"] = self.id
        self.dal.create_one(**kwargs)

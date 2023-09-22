from db.dal.user import UserDAL
from db.client import session_maker


class UserService:
    def __init__(self, user_id):
        self.user_id = user_id
        self.instance = UserDAL(session_maker).get_one_or_none(id=user_id)

    def ban(self):
        if not self.instance.banned:
            UserDAL(session_maker).update_one(
                {"admin": False, "pending": False, "subscriber": False, "banned": True},
                id=self.user_id,
            )  # можно ли както сделать на уровне таблицы эту логику когда при бане все поля становятся False
        else:
            raise Exception("Already banned")

    def add(self):
        if not self.instance.subscriber:
            UserDAL(session_maker).update_one(
                {"pending": False, "subscriber": True}, id=self.user_id
            )
        else:
            raise Exception("Already added")

    def make_admin(self):
        if not self.instance.admin:
            UserDAL(session_maker).update_one({"admin": True}, id=self.user_id)
        else:
            raise Exception("Already admin")

    def refusal(self):
        if self.instance is not None:
            UserDAL(session_maker).delete_one(id=self.user_id)
        else:
            raise Exception("Already refusaled")

    def create(self, **kwargs):
        if self.instance is None:
            kwargs["id"] = self.user_id
            UserDAL(session_maker).create_one(**kwargs)
        else:
            raise Exception("Already created")

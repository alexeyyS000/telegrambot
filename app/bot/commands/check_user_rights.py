def check_admin(funk):
    async def inner(*args, **kwargs):
        if kwargs["user"] is None or not kwargs["user"].admin:
            return 1
        kwargs.pop("state", None)
        kwargs.pop("raw_state", None)
        kwargs.pop("user", None)
        await funk(*args, **kwargs)

    return inner


def check_registrated_user(funk):
    async def inner(*args, **kwargs):
        if kwargs["user"] is not None:
            return 1
        kwargs.pop(
            "raw_state", None
        )  # не знаю как обойтись без костыля так как func иногда принимает лишние аргументы, их приходится удалять
        kwargs.pop("user", None)
        await funk(*args, **kwargs)

    return inner

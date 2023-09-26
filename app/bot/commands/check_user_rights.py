def check_admin(funk):
    async def inner(*args, **kwargs):
        if kwargs["user"] is None or not kwargs["user"].admin:
            return 1
        await funk(*args)

    return inner


def check_unregistrated_user(funk):
    async def inner(*args, **kwargs):
        if kwargs["user"] is not None:
            return 1
        print(args)
        await funk(*args)

    return inner

from . import Context


class Users(object):
    def __init__(self):
        self._users = []

    def add_user(self, user: Context):
        self._users.append(user)

    def get_user_by_tg_id(self, tg_id):
        for user in self._users:
            if user.tg_id == tg_id:
                return user
        return None
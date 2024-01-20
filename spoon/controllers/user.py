from ..models.user import User


class UserController:
    @staticmethod
    def get_all():
        return list(map(User.get, User.all_pks()))

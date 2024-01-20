from redis_om import Migrator
from ..models.user import User
from uuid import uuid5


def generate_users():
    Migrator().run()
    admin_user = User(
        first_name="Admin", last_name="User", email="admin.user@company.foo", password=str(uuid5)
    )
    if not User.find(User.email == admin_user.email).all():
        admin_user.save()

    regular_user = User(
        first_name="Regular",
        last_name="User",
        email="regular.user@company.foo",
        password=str(uuid5),
    )
    if not User.find(User.email == regular_user.email).all():
        regular_user.save()

    for n in range(10):
        n_user = User(
            first_name=f"User {n}",
            last_name="Brocoli",
            email=f"{n}.brocoli@company.foo",
            password=str(uuid5),
        )
        if not User.find(User.email == n_user.email).all():
            n_user.save()

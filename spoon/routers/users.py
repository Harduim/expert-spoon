from fastapi import APIRouter
from ..models.views.user import User
from ..controllers.user import UserController

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_all_users() -> list[User]:
    """List of all users

    Returns
    -------
    list[User]
    """

    # Bizarre, but I could figure out another way to do this
    return UserController.get_all()

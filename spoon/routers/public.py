from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter(prefix="", tags=["Public"])


@router.get("/")
async def redirect_default():
    return RedirectResponse("/docs", 302)


@router.get("/health")
async def health_check():
    return {"Ok": "Ok"}

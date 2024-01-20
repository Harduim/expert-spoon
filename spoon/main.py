from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def api() -> FastAPI:
    return api_factory(
        title="Expert Spoon Backend",
        allow_origins=["http://localhost:3003"],
    )


def api_factory(title: str, allow_origins: list[str]) -> FastAPI:
    from .routers import public

    app = FastAPI(title=title)
    app.include_router(router=public.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

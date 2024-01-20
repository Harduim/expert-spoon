import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "spoon.main:api",
        port=3003,
        log_level="debug",
        reload=True,
        headers=[],
        reload_dirs=["spoon"],
        reload_delay=2,
        factory=True,
    )

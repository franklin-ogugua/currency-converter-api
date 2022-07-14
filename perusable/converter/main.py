import logging

from fastapi import FastAPI

from converter.api import currency_crud, ping, users

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    """
    Wires up the router up to the main app, and uses a
    function to initialize a new app.
    """
    application = FastAPI()

    application.include_router(ping.router)
    application.include_router(users.router)
    application.include_router(currency_crud.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

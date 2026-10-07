from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

import config

app = FastAPI()

@lru_cache
def get_settings():
    return config.Settings()


@app.get("/")
def index():
    return {"Message": "Hello World"}


@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user
    }
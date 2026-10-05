from fastapi import FastAPI, Depends
import config
from typing import Annotated
from functools import lru_cache



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
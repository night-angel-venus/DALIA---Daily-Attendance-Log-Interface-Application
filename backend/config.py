from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):

    # Static Info
    app_name:str = os.getenv("APP_NAME")
    admin_email:str = os.getenv("ADMIN_EMAIL")
    items_per_user: int = 50

    # Database URL
    # TODO: Configure into database.py

    database_url: str = os.getenv("DATABASE_URL")

    model_config = SettingsConfigDict(env_file = ".env")


settings = Settings()
from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=find_dotenv(), extra="ignore")
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"


settings = Settings()

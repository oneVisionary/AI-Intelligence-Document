from pydantic_settings import BaseSettings
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME:str
    DATABASE_URL:str
    UPLOAD_DIR:str
    LOG_LEVEL:str
    REDIS_URL:str
    


    class Config:
        env_file =BASE_DIR/".env"

settings = Settings()
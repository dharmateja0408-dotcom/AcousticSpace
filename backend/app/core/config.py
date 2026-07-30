

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME = "AcousticSpace"

    VERSION = "1.0"

    UPLOAD_DIR = "app/uploads"

    MAX_UPLOAD_SIZE = 100

    class Config:
        env_file = ".env"


settings = Settings()
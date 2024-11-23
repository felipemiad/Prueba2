from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ICFES API"
    MODEL_VERSION: str = "1.0.0"

    class Config:
        case_sensitive = True


settings = Settings()

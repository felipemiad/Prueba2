import logging
import sys
from loguru import logger
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "API de Predicciones ICFES"

    # Configuración de CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:3000",
        "https://localhost:8000",
        "https://localhost:3000",
    ]  # Ajusta estos valores según las necesidades

    class Config:
        case_sensitive = True


# Función para configurar los logs
def setup_app_logging():
    """Configura el logger para la aplicación."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    logger.info("Logging configurado correctamente.")


# Instancia de configuración
settings = Settings()


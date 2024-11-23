import logging
import sys
from loguru import logger
from pydantic import BaseSettings


# Configuración básica de la aplicación
class Settings(BaseSettings):
    PROJECT_NAME: str = "ICFES API"
    API_V1_STR: str = "/api/v1"

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

from typing import Any

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

# Configurar logging
setup_app_logging()

# Crear instancia de FastAPI
app = FastAPI(
    title="API de Predicciones ICFES",
    description="API para realizar predicciones basadas en datos del ICFES utilizando Gradient Boosting",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Definir un router raíz para bienvenida
root_router = APIRouter()

@root_router.get("/")
def index(request: Request) -> Any:
    """
    Respuesta HTML básica en la raíz.
    """
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Bienvenido a la API de Predicciones ICFES</h1>"
        "<div>"
        "Consulta la documentación interactiva aquí: <a href='/docs'>Documentación</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)

# Incluir el router de las rutas de predicción
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# Configurar CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == "__main__":
    # Advertencia para uso en desarrollo
    logger.warning("Ejecutando en modo desarrollo. No usar esta configuración en producción.")
    import uvicorn

    # Ejecutar el servidor en el puerto 8000
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

from fastapi import FastAPI, APIRouter
from app.config import settings, setup_app_logging
from app.api import api_router

# Configurar el logging
setup_app_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Rutas principales
root_router = APIRouter()


@root_router.get("/")
def index():
    return {"message": "Bienvenido a la API de ICFES"}

# Incluir rutas
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

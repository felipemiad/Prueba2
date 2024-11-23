from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router
from app.config import settings, setup_app_logging

# Configurar logging
setup_app_logging(config=settings)

# Crear la aplicación FastAPI
app = FastAPI(
    title="ICFES API",
    description="API para realizar predicciones con el modelo del ICFES",
    version="1.0.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar según las necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(api_router)

# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "¡Bienvenido a la API del ICFES!"}

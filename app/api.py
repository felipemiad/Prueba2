from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from loguru import logger
import pandas as pd
from model_pkg.predictor import make_prediction

# Esquemas de entrada y salida
class MultipleDataInputs(BaseModel):
    inputs: list[dict]

class PredictionResults(BaseModel):
    errors: str = None
    version: str
    predictions: list = None

# Instancia del router
api_router = APIRouter()

@api_router.get("/health", status_code=200)
def health():
    """
    Endpoint para verificar el estado del modelo.
    """
    return {"status": "ok", "model_version": "1.0.0"}

@api_router.post("/predict", response_model=PredictionResults, status_code=200)
async def predict(input_data: MultipleDataInputs):
    """
    Realiza predicciones usando el modelo Gradient Boosting.
    """
    logger.info("Recibiendo datos de entrada para predicción.")
    try:
        # Convertir los datos de entrada en un DataFrame
        input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
        logger.info(f"Datos de entrada: {input_df.to_dict(orient='records')}")

        # Llamar a la función `make_prediction` del predictor
        results = make_prediction(input_df)

        if results["errors"]:
            logger.error(f"Errores durante la predicción: {results['errors']}")
            raise HTTPException(status_code=400, detail=results["errors"])

        logger.info(f"Predicciones generadas: {results['predictions']}")
        return {
            "errors": None,
            "version": "1.0.0",
            "predictions": results["predictions"],
        }

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error durante la predicción")

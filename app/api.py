from fastapi import APIRouter, HTTPException
from app.schemas import PredictionResults, MultipleDataInputs
from model_pkg.predictor import GradientBoostingModel

# Instancia del modelo
model = GradientBoostingModel(data_path="data/df_definitivo.csv")

api_router = APIRouter()

@api_router.get("/health", status_code=200)
def health():
    return {"status": "ok", "model_version": "1.0.0"}

@api_router.post("/predict", response_model=PredictionResults, status_code=200)
async def predict(input_data: MultipleDataInputs):
    """
    Realiza predicciones usando el modelo Gradient Boosting.
    """
    try:
        predictions = model.predict(input_data.inputs)
        return {
            "errors": None,
            "version": "1.0.0",
            "predictions": predictions,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

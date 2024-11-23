import numpy as np
import pandas as pd
import joblib
from typing import Dict, Any

# Ruta del modelo previamente entrenado
MODEL_PATH = "model_pkg/model_icfes.pkl"  # Asegúrate de que este archivo exista en la ubicación correcta

# Cargar el modelo
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise ValueError(f"Error cargando el modelo: {str(e)}")

# Variables necesarias para el modelo
VARIABLES_FINALES = [
    "FAMI_ESTRATOVIVIENDA",
    "FAMI_PERSONASHOGAR",
    "FAMI_TIENEINTERNET",
    "ESTU_HORASSEMANATRABAJA",
    "FAMI_COMECARNEPESCADOHUEVO",
    "COLE_NATURALEZA",
    "ESTU_DEPTO_RESIDE",
    "COLE_JORNADA",
    "COLE_GENERO",
]

def make_prediction(input_data: pd.DataFrame) -> Dict[str, Any]:
    """
    Realiza una predicción usando el modelo cargado.

    Parameters
    ----------
    input_data : pd.DataFrame
        Datos de entrada en formato DataFrame.

    Returns
    -------
    Dict[str, Any]
        Un diccionario que contiene las predicciones y posibles errores.
    """
    result = {"predictions": None, "errors": None}

    try:
        # Validar que las columnas necesarias están presentes en el DataFrame
        missing_cols = set(VARIABLES_FINALES) - set(input_data.columns)
        if missing_cols:
            result["errors"] = f"Faltan las columnas requeridas: {missing_cols}"
            return result

        # Realizar predicciones
        predictions = model.predict(input_data[VARIABLES_FINALES])
        result["predictions"] = predictions.tolist()

    except Exception as e:
        result["errors"] = str(e)

    return result

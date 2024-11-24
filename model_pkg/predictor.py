import joblib
import pandas as pd
from typing import Dict, Any

# Ruta del modelo y encoder
MODEL_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/model_icfes.pkl"
ENCODER_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/encoder_icfes.pkl"

# Cargar modelo y encoder
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

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
        # Validar que las columnas necesarias están presentes
        missing_cols = set(VARIABLES_FINALES) - set(input_data.columns)
        if missing_cols:
            result["errors"] = f"Faltan columnas requeridas: {missing_cols}"
            return result

        # Codificar los datos de entrada
        input_encoded = encoder.transform(input_data[VARIABLES_FINALES])

        # Realizar predicciones
        predictions = model.predict(input_encoded)
        result["predictions"] = predictions.tolist()

    except Exception as e:
        result["errors"] = str(e)

    return result

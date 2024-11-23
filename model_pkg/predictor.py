import pandas as pd
import joblib
from typing import Dict, Any

# Rutas de los archivos del modelo y encoder
MODEL_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/model_icfes.pkl"  # Ruta del modelo
ENCODER_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/encoder_icfes.pkl"  # Ruta del encoder

# Variables finales necesarias para el modelo
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

# Cargar el modelo y el encoder
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

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
            result["errors"] = f"Faltan las columnas requeridas: {missing_cols}"
            return result

        # Ordenar las columnas según VARIABLES_FINALES
        input_data = input_data[VARIABLES_FINALES]

        # Codificar los datos de entrada
        input_encoded = encoder.transform(input_data)

        # Realizar las predicciones
        predictions = model.predict(input_encoded)
        result["predictions"] = predictions.tolist()

    except Exception as e:
        result["errors"] = str(e)

    return result

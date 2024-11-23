<<<<<<< HEAD
=======
import numpy as np
>>>>>>> 66eca488ff3c8b50058709080352271dbb2ac608
import pandas as pd
import joblib
from typing import Dict, Any
from loguru import logger

<<<<<<< HEAD
# Rutas de los archivos del modelo y encoder
MODEL_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/model_icfes.pkl"  # Ruta del modelo
ENCODER_PATH = "C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/encoder_icfes.pkl"  # Ruta del encoder
=======
# Ruta del modelo previamente entrenado
MODEL_PATH = "model_pkg/model_icfes.pkl"
logger.info(f"Cargando el modelo desde {MODEL_PATH}...")
model = joblib.load(MODEL_PATH)
logger.info("Modelo cargado correctamente.")
>>>>>>> 66eca488ff3c8b50058709080352271dbb2ac608

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
        logger.info("Validando las columnas en los datos de entrada...")
        # Validar que las columnas necesarias están presentes en el DataFrame
        missing_cols = set(VARIABLES_FINALES) - set(input_data.columns)
        if missing_cols:
            result["errors"] = f"Faltan las columnas requeridas: {missing_cols}"
<<<<<<< HEAD
            return result

        # Ordenar las columnas según VARIABLES_FINALES
        input_data = input_data[VARIABLES_FINALES]

        # Codificar los datos de entrada
        input_encoded = encoder.transform(input_data)

        # Realizar las predicciones
        predictions = model.predict(input_encoded)
=======
            logger.error(result["errors"])
            return result

        # Reordenar las columnas para que coincidan con el orden esperado por el modelo
        input_data = input_data[VARIABLES_FINALES]
        logger.info(f"Datos después de validar y reordenar: {input_data.head()}")

        # Realizar predicciones
        logger.info("Realizando predicción con el modelo...")
        predictions = model.predict(input_data)
>>>>>>> 66eca488ff3c8b50058709080352271dbb2ac608
        result["predictions"] = predictions.tolist()
        logger.info(f"Predicciones realizadas con éxito: {result['predictions']}")

    except Exception as e:
        result["errors"] = str(e)
        logger.error(f"Error durante la predicción: {str(e)}")

    return result

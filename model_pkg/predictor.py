import pandas as pd
import joblib
from typing import Dict, Any
from loguru import logger

# Cargar el modelo y el encoder
MODEL_PATH = "model_pkg/model_icfes.pkl"
ENCODER_PATH = "model_pkg/encoder_icfes.pkl"
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

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

def make_prediction(input_data: pd.DataFrame) -> Dict[str, Any]:
    """
    Realiza una predicción usando el modelo y el encoder cargados.

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
            logger.error(result["errors"])
            return result

        logger.info(f"Datos originales:\n{input_data.head()}")
        logger.info(f"Tipos de datos originales:\n{input_data.dtypes}")

        # Asegurarse de que los tipos de datos son consistentes
        for col in VARIABLES_FINALES:
            input_data[col] = input_data[col].astype(str)

        logger.info(f"Datos después de transformar a tipo 'str':\n{input_data.head()}")
        logger.info(f"Tipos de datos después de transformar:\n{input_data.dtypes}")

        # Codificar las variables categóricas, categorías desconocidas serán -1
        input_data_encoded = encoder.transform(input_data[VARIABLES_FINALES])
        logger.info(f"Datos codificados:\n{input_data_encoded}")

        # Realizar predicciones
        logger.info("Realizando predicción con el modelo...")
        predictions = model.predict(input_data_encoded)
        result["predictions"] = predictions.tolist()

    except Exception as e:
        result["errors"] = str(e)
        logger.error(f"Error durante la predicción: {str(e)}")

    return result

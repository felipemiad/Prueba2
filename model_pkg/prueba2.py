import pandas as pd
from .predictor import make_prediction


# Datos de entrada de prueba
data = pd.DataFrame([{
    "FAMI_ESTRATOVIVIENDA": "Estrato 2",
    "FAMI_PERSONASHOGAR": 4,
    "FAMI_TIENEINTERNET": "Sí",
    "ESTU_HORASSEMANATRABAJA": 10,
    "FAMI_COMECARNEPESCADOHUEVO": "Diariamente",
    "COLE_NATURALEZA": "Oficial",
    "ESTU_DEPTO_RESIDE": "Antioquia",
    "COLE_JORNADA": "Mañana",
    "COLE_GENERO": "Mixto"
}])

# Prueba la predicción
result = make_prediction(data)
print(result)

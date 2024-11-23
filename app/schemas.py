from typing import List, Optional
from pydantic import BaseModel

# Esquema para la entrada
class DataInput(BaseModel):
    FAMI_ESTRATOVIVIENDA: int
    FAMI_PERSONASHOGAR: int
    FAMI_TIENEINTERNET: int
    ESTU_HORASSEMANATRABAJA: int
    FAMI_COMECARNEPESCADOHUEVO: int
    COLE_NATURALEZA: str
    ESTU_DEPTO_RESIDE: str
    COLE_JORNADA: str
    COLE_GENERO: str

# Esquema para múltiples entradas
class MultipleDataInputs(BaseModel):
    inputs: List[DataInput]

# Esquema para los resultados
class PredictionResults(BaseModel):
    errors: Optional[str]
    version: str
    predictions: List[float]

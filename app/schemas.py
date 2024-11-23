from typing import List, Optional
from pydantic import BaseModel

class InputData(BaseModel):
    ESTU_GENERO: str
    ESTU_DEPTO_RESIDE: str
    FAMI_ESTRATOVIVIENDA: str
    FAMI_PERSONASHOGAR: int
    FAMI_TIENEINTERNET: str
    ESTU_HORASSEMANATRABAJA: int
    FAMI_COMECARNEPESCADOHUEVO: str
    COLE_JORNADA: str
    COLE_GENERO: str
    COLE_NATURALEZA: str

class MultipleDataInputs(BaseModel):
    inputs: List[InputData]

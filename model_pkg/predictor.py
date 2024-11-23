import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

class GradientBoostingModel:
    def __init__(self, data_path="data/df_definitivo.csv"):
        """
        Inicializa el modelo, carga los datos y entrena el modelo.
        :param data_path: Ruta al archivo CSV con los datos.
        """
        self.data_path = data_path
        self.model = GradientBoostingRegressor(
            n_estimators=100, learning_rate=0.1, max_depth=3, random_state=0
        )
        self.variables_finales = [
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
        self._load_and_train()

    def _load_and_train(self):
        """
        Carga los datos desde el archivo CSV y ent

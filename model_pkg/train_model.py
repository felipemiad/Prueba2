import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

# Cargar datos
df = pd.read_csv("data/df_definitivo.csv")
variables_finales = [
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

X = df[variables_finales]
y = df["PUNT_GLOBAL"]

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=0)

# Preprocesar y entrenar modelo
encoder = OrdinalEncoder()
X_train_enc = encoder.fit_transform(X_train)
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train_enc, y_train)

# Guardar modelo y preprocesador
with open("model_pkg/model.pkl", "wb") as model_file:
    pickle.dump((model, encoder), model_file)

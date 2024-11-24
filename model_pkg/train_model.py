import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import joblib

# Ruta del archivo CSV
DATA_PATH = "model_pkg/df_definitivo.csv"  # Cambia la ruta si es necesario

# Variables finales que necesita el modelo
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

# Cargar el dataset
df = pd.read_csv(DATA_PATH)

# Dividir los datos
X = df[VARIABLES_FINALES]
y = df["PUNT_GLOBAL"]

# Codificar variables categóricas
from sklearn.preprocessing import OrdinalEncoder

# Configurar el encoder
encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
X_encoded = encoder.fit_transform(X)

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo y el encoder
joblib.dump(model, "model_pkg/model_icfes.pkl")
joblib.dump(encoder, "model_pkg/encoder_icfes.pkl")

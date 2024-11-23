import joblib

# Cargar el modelo
model = joblib.load("C:/Users/johan/Documents/Maestria/Despliegue Analitica/ProyectoIcfes/icfes-api/model_pkg/model_icfes.pkl")
print(type(model))  # Debería mostrar: <class 'sklearn.ensemble._gb.GradientBoostingRegressor'>

# Verificar que el modelo tiene el método predict
print(hasattr(model, "predict"))  # Debería devolver: True

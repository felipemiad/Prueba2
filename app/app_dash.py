import dash
from dash import dcc, html, Input, Output, State
import requests

# Inicializar la aplicación Dash
app = dash.Dash(__name__)
app.title = "Tablero de Predicción ICFES"

# Layout del tablero
app.layout = html.Div([
    html.H1("Predicción del Puntaje Global - ICFES", style={"textAlign": "center"}),

    # Entradas para las variables
    html.Div([
        html.Label("Estrato de Vivienda:"),
        dcc.Input(id="input_estrato", type="text", placeholder="Estrato (Ejemplo: Estrato 2)"),

        html.Label("Personas en el Hogar:"),
        dcc.Input(id="input_personas_hogar", type="number", placeholder="Número de Personas"),

        html.Label("¿Tiene Internet?:"),
        dcc.Dropdown(
            id="input_internet",
            options=[
                {"label": "Sí", "value": "Sí"},
                {"label": "No", "value": "No"},
            ],
            placeholder="Seleccione una opción"
        ),

        html.Label("Horas Semanales que Trabaja:"),
        dcc.Input(id="input_horas_trabaja", type="number", placeholder="Horas Semanales"),

        html.Label("Frecuencia de Consumo de Carne, Pescado o Huevo:"),
        dcc.Input(id="input_comida", type="text", placeholder="Frecuencia (Ejemplo: Diario)"),

        html.Label("Naturaleza del Colegio:"),
        dcc.Input(id="input_naturaleza", type="text", placeholder="Ejemplo: Oficial"),

        html.Label("Departamento donde Reside:"),
        dcc.Input(id="input_departamento", type="text", placeholder="Ejemplo: Antioquia"),

        html.Label("Jornada del Colegio:"),
        dcc.Input(id="input_jornada", type="text", placeholder="Ejemplo: Mañana"),

        html.Label("Género del Colegio:"),
        dcc.Input(id="input_genero", type="text", placeholder="Ejemplo: Mixto"),
    ], style={"margin": "20px"}),

    # Botón para enviar los datos
    html.Button("Predecir", id="predict_button", n_clicks=0, style={"margin": "10px"}),

    # Mostrar resultados de la predicción
    html.Div(id="prediction_result", style={"marginTop": "20px", "textAlign": "center"})
])

---

### 2. Definir la interacción con la API

```python
# Función callback para procesar los datos y obtener la predicción
@app.callback(
    Output("prediction_result", "children"),
    [Input("predict_button", "n_clicks")],
    [
        State("input_estrato", "value"),
        State("input_personas_hogar", "value"),
        State("input_internet", "value"),
        State("input_horas_trabaja", "value"),
        State("input_comida", "value"),
        State("input_naturaleza", "value"),
        State("input_departamento", "value"),
        State("input_jornada", "value"),
        State("input_genero", "value"),
    ],
)
def obtener_prediccion(n_clicks, estrato, personas_hogar, internet, horas_trabaja, comida, naturaleza, departamento, jornada, genero):
    if n_clicks > 0:
        # Crear el payload con los datos ingresados
        payload = {
            "inputs": [
                {
                    "FAMI_ESTRATOVIVIENDA": estrato,
                    "FAMI_PERSONASHOGAR": personas_hogar,
                    "FAMI_TIENEINTERNET": internet,
                    "ESTU_HORASSEMANATRABAJA": horas_trabaja,
                    "FAMI_COMECARNEPESCADOHUEVO": comida,
                    "COLE_NATURALEZA": naturaleza,
                    "ESTU_DEPTO_RESIDE": departamento,
                    "COLE_JORNADA": jornada,
                    "COLE_GENERO": genero,
                }
            ]
        }

        try:
            # Hacer la solicitud POST a la API
            response = requests.post("http://54.226.170.98:8000/api/v1/predict", json=payload)

            if response.status_code == 200:
                prediction = response.json()["predictions"][0]
                return html.Div([
                    html.H3(f"Predicción del Puntaje Global: {prediction:.2f}", style={"color": "green"})
                ])
            else:
                return html.Div([
                    html.H3(f"Error: {response.json().get('detail', 'Algo salió mal')}", style={"color": "red"})
                ])
        except Exception as e:
            return html.Div([
                html.H3(f"Error al conectar con la API: {str(e)}", style={"color": "red"})
            ])
    return ""

---

### 3. Correr la aplicación Dash

```python
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)

from flask import Flask, render_template, request
from utilities import predecir, ModeloNoEncontradoError

app = Flask(__name__)


def validar_entrada(engine_size, cylinders, fuel_consumption):
    """
    Valida y convierte los datos recibidos desde el formulario.

    Rangos realistas usados:
    - engine_size: entre 0.5 y 10 litros
    - cylinders: entre 1 y 16
    - fuel_consumption: entre 0.1 y 30 L/100 km

    Devuelve:
    - tupla con valores convertidos si todo es correcto
    - None si hay datos inválidos
    """
    try:
        engine_size = float(engine_size)
        cylinders = int(cylinders)
        fuel_consumption = float(fuel_consumption)

        if engine_size < 0.5 or engine_size > 10:
            return None

        if cylinders < 1 or cylinders > 16:
            return None

        if fuel_consumption < 0.1 or fuel_consumption > 30:
            return None

        return engine_size, cylinders, fuel_consumption

    except (ValueError, TypeError):
        return None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    datos_validados = validar_entrada(
        request.form.get("engine_size"),
        request.form.get("cylinders"),
        request.form.get("fuel_consumption")
    )

    if datos_validados is None:
        return render_template(
            "home.html",
            error="Datos inválidos. Introduce valores numéricos y dentro de un rango realista."
        )

    engine_size, cylinders, fuel_consumption = datos_validados

    try:
        resultado = predecir(engine_size, cylinders, fuel_consumption)
        return render_template("home.html", resultado=resultado)

    except ModeloNoEncontradoError:
        return render_template(
            "home.html",
            error="No se encuentra el modelo. Coloca el archivo pipeline.pickle dentro de la carpeta models/."
        )

    except Exception as e:
        return render_template(
            "home.html",
            error=f"Ha ocurrido un error al realizar la predicción: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)

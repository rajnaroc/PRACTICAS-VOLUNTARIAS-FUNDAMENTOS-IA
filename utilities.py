import pickle
from pathlib import Path

import pandas as pd


MODEL_PATH = Path(__file__).resolve().parent / "models" / "pipeline.pickle"


class ModeloNoEncontradoError(FileNotFoundError):
    """Error personalizado para indicar que falta el archivo del modelo."""
    pass


_modelo_cache = None


def cargar_modelo():
    """
    Carga el modelo entrenado desde models/pipeline.pickle.

    Se usa caché para no abrir el archivo en cada predicción.
    """
    global _modelo_cache

    if _modelo_cache is not None:
        return _modelo_cache

    if not MODEL_PATH.exists():
        raise ModeloNoEncontradoError(f"No existe el archivo: {MODEL_PATH}")

    with open(MODEL_PATH, "rb") as archivo:
        _modelo_cache = pickle.load(archivo)

    return _modelo_cache


def predecir(engine_size, cylinders, fuel_consumption):
    """
    Recibe los datos del vehículo, crea un DataFrame con las mismas columnas
    usadas durante el entrenamiento y devuelve la predicción redondeada.
    """
    modelo = cargar_modelo()

    datos = pd.DataFrame({
        "ENGINESIZE": [float(engine_size)],
        "CYLINDERS": [int(cylinders)],
        "FUELCONSUMPTION_COMB": [float(fuel_consumption)]
    })

    prediccion = modelo.predict(datos)
    return round(float(prediccion[0]), 2)

# P1CO2 - Webapp Flask para predecir emisiones de CO₂

Este proyecto implementa una aplicación web con Flask que usa un modelo de Machine Learning para predecir las emisiones de CO₂ de un vehículo.

## Objetivo

La aplicación recibe tres datos:

- ENGINESIZE
- CYLINDERS
- FUELCONSUMPTION_COMB

Y devuelve una predicción:

- CO2EMISSIONS

## Estructura del proyecto

```text
P1CO2/
├── app.py
├── utilities.py
├── requirements.txt
├── models/
│   └── pipeline.pickle
├── templates/
│   └── home.html
└── notebooks/
    └── entrenamiento_colab.ipynb
```

## Paso 1: entrenar el modelo

Abre el notebook:

```text
notebooks/entrenamiento_colab.ipynb
```

en Google Colab.

Después sube el archivo:

```text
FuelConsumption.csv
```

Ejecuta todas las celdas y descarga el archivo generado:

```text
pipeline.pickle
```

## Paso 2: colocar el modelo

Copia `pipeline.pickle` dentro de:

```text
models/pipeline.pickle
```

## Paso 3: crear entorno virtual

Dentro de la carpeta del proyecto:

```bash
python -m venv venv
```

Activar entorno virtual en Linux:

```bash
source venv/bin/activate
```

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## Paso 4: instalar dependencias

```bash
pip install -r requirements.txt
```

## Paso 5: ejecutar la aplicación

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Prueba recomendada

Puedes probar con estos valores:

- Tamaño del motor: 2.0
- Cilindros: 4
- Consumo combinado: 8.5

## Seguridad añadida

El proyecto incluye validación básica en backend para evitar:

- valores negativos
- texto en vez de números
- valores extremos
- datos fuera de rangos realistas

Esto evita predicciones absurdas y errores de ejecución.

## Explicación breve

`app.py` contiene la lógica de la web con Flask.

`utilities.py` carga el modelo guardado en `models/pipeline.pickle` y realiza la predicción.

`home.html` contiene el formulario web que ve el usuario.
# PR-CTICAS-VOLUNTARIAS-FUNDAMENTOS-IA
# PR-CTICAS-VOLUNTARIAS-FUNDAMENTOS-IA

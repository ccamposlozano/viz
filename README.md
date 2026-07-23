# simple_eda

Un paquete de Python **diminuto** para análisis exploratorio de datos (EDA)
sobre DataFrames de [pandas](https://pandas.pydata.org/). Dos funciones, una
sola dependencia, cero complicaciones.

```python
import pandas as pd
import matplotlib.pyplot as plt
import simple_eda as eda

df = pd.read_csv("data.csv")
eda.summarize(df)      # forma, tipos y estadísticas por columna
eda.missing(df)        # valores faltantes por columna

eda.histograms(df)     # un histograma por columna numérica
eda.boxplots(df)       # un boxplot por columna numérica
plt.show()
```

## Instalación

Desde el código fuente (modo desarrollo, recomendado en clase):

```bash
pip install -e .
```

O una vez publicado en PyPI:

```bash
pip install simple_eda
```

## Funciones

### `summarize(df, verbose=True)`

Imprime y devuelve un resumen del DataFrame: número de filas y columnas y,
por cada columna, su tipo (`dtype`), cuántos valores no nulos y nulos tiene,
cuántos valores únicos, y `min`/`max`/`mean` para las columnas numéricas.

```python
resumen = eda.summarize(df)   # devuelve un DataFrame para seguir usándolo
```

### `missing(df, verbose=True)`

Imprime y devuelve las columnas con valores faltantes, ordenadas de mayor a
menor, con el conteo y el porcentaje sobre el total de filas.

```python
faltantes = eda.missing(df)
```

Pasa `verbose=False` si solo quieres el DataFrame de resultado sin que se
imprima nada.

### `histograms(df, bins=20, save=None)`

Dibuja con **matplotlib** un histograma por cada columna numérica del
DataFrame (en una cuadrícula). Devuelve la figura de matplotlib; muéstrala con
`plt.show()` o guárdala pasando `save="hist.png"`.

```python
import matplotlib.pyplot as plt
eda.histograms(df, bins=15)
plt.show()
```

### `boxplots(df, save=None)`

Dibuja con **matplotlib** un boxplot por cada columna numérica — ideal para
ver la mediana, los cuartiles y los valores atípicos. Igual que arriba,
devuelve la figura y acepta `save`.

```python
eda.boxplots(df, save="cajas.png")
```

Las columnas no numéricas se ignoran automáticamente en ambas funciones.

## Ejemplo completo

```python
import pandas as pd
import simple_eda as eda

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", None],
    "edad": [23, 35, None, 41],
    "ciudad": ["SF", "SF", "LA", "LA"],
})

eda.summarize(df)
eda.missing(df)

import matplotlib.pyplot as plt
eda.histograms(df)
eda.boxplots(df)
plt.show()
```

## Publicar en PyPI

Este proyecto se construye con [Hatchling](https://hatch.pypa.io/). Para
generar los artefactos y subirlos:

```bash
python -m pip install --upgrade build twine
python -m build                       # crea dist/*.whl y dist/*.tar.gz
python -m twine upload --repository testpypi dist/*   # primero a TestPyPI
python -m twine upload dist/*                          # luego a PyPI
```

> Nota: el nombre `simple_eda` puede ya estar tomado en PyPI/TestPyPI. Si el
> subir falla por nombre duplicado, cambia `name` en `pyproject.toml` por uno
> único (por ejemplo `simple-eda-tuusuario`) y vuelve a construir.

## Requisitos

- Python 3.8+
- pandas
- matplotlib

## Licencia

MIT

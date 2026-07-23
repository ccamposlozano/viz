"""Gráficas de EDA con matplotlib.

Funciones sencillas que dibujan las columnas numéricas de un DataFrame.
Cada una crea una figura de matplotlib y la devuelve, para que puedas
mostrarla (``plt.show()``) o guardarla (parámetro ``save``).

    import pandas as pd
    import matplotlib.pyplot as plt
    import simple_eda as eda

    df = pd.read_csv("data.csv")
    eda.histograms(df)
    eda.boxplots(df)
    plt.show()
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import pandas as pd


def _numeric_columns(df: pd.DataFrame) -> list[str]:
    """Devuelve los nombres de las columnas numéricas del DataFrame."""
    return [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]


def histograms(df: pd.DataFrame, bins: int = 20, save: str | None = None):
    """Dibuja un histograma por cada columna numérica.

    Parameters
    ----------
    df:
        El DataFrame a graficar.
    bins:
        Número de barras de cada histograma (por defecto 20).
    save:
        Si se indica una ruta, guarda la figura en ese archivo.

    Returns
    -------
    matplotlib.figure.Figure
        La figura creada (aún no mostrada; llama a ``plt.show()``).
    """
    cols = _numeric_columns(df)
    if not cols:
        raise ValueError("No hay columnas numéricas para graficar.")

    n = len(cols)
    ncols = min(3, n)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 3 * nrows))
    axes = _flatten_axes(axes)

    for ax, col in zip(axes, cols):
        df[col].dropna().plot(kind="hist", bins=bins, ax=ax, edgecolor="white")
        ax.set_title(col)
        ax.set_ylabel("frecuencia")

    for ax in axes[n:]:  # apaga los ejes sobrantes de la cuadrícula
        ax.set_visible(False)

    fig.suptitle("Histogramas", fontsize=13, fontweight="bold")
    fig.tight_layout()

    if save:
        fig.savefig(save, dpi=120, bbox_inches="tight")
    return fig


def boxplots(df: pd.DataFrame, save: str | None = None):
    """Dibuja un boxplot por cada columna numérica (una caja por columna).

    Parameters
    ----------
    df:
        El DataFrame a graficar.
    save:
        Si se indica una ruta, guarda la figura en ese archivo.

    Returns
    -------
    matplotlib.figure.Figure
        La figura creada (aún no mostrada; llama a ``plt.show()``).
    """
    cols = _numeric_columns(df)
    if not cols:
        raise ValueError("No hay columnas numéricas para graficar.")

    n = len(cols)
    ncols = min(3, n)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.2 * ncols, 3.2 * nrows))
    axes = _flatten_axes(axes)

    for ax, col in zip(axes, cols):
        ax.boxplot(df[col].dropna())
        ax.set_xticks([1])
        ax.set_xticklabels([col])
        ax.set_title(col)

    for ax in axes[n:]:
        ax.set_visible(False)

    fig.suptitle("Boxplots", fontsize=13, fontweight="bold")
    fig.tight_layout()

    if save:
        fig.savefig(save, dpi=120, bbox_inches="tight")
    return fig


def _flatten_axes(axes):
    """Convierte la salida de subplots (Axes, array o array 2D) en una lista."""
    if hasattr(axes, "flatten"):
        return list(axes.flatten())
    return [axes]

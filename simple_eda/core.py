"""Funciones principales de simple_eda.

Dos funciones sencillas para echar un primer vistazo a un DataFrame:

- ``summarize(df)``: forma, tipos y estadísticas básicas por columna.
- ``missing(df)``: conteo y porcentaje de valores faltantes por columna.

Cada función imprime un resumen legible y además devuelve un
``pandas.DataFrame`` para poder seguir trabajando con el resultado.
"""

from __future__ import annotations

import pandas as pd


def summarize(df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """Resume un DataFrame: forma, tipo y estadísticas básicas por columna.

    Parameters
    ----------
    df:
        El DataFrame a resumir.
    verbose:
        Si es ``True`` (por defecto) imprime el resumen. En todos los casos
        se devuelve el resultado como DataFrame.

    Returns
    -------
    pandas.DataFrame
        Una fila por columna del DataFrame original, con estas columnas:
        ``dtype``, ``non_null``, ``nulls``, ``unique``, ``min``, ``max``,
        ``mean``.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("summarize() espera un pandas.DataFrame")

    rows = []
    for col in df.columns:
        s = df[col]
        info = {
            "column": col,
            "dtype": str(s.dtype),
            "non_null": int(s.notna().sum()),
            "nulls": int(s.isna().sum()),
            "unique": int(s.nunique(dropna=True)),
            "min": None,
            "max": None,
            "mean": None,
        }
        if pd.api.types.is_numeric_dtype(s):
            info["min"] = s.min()
            info["max"] = s.max()
            info["mean"] = round(float(s.mean()), 4) if info["non_null"] else None
        rows.append(info)

    result = pd.DataFrame(rows).set_index("column")

    if verbose:
        n_rows, n_cols = df.shape
        print(f"DataFrame: {n_rows} filas x {n_cols} columnas")
        print("-" * 40)
        print(result.to_string())

    return result


def missing(df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """Reporta los valores faltantes por columna.

    Parameters
    ----------
    df:
        El DataFrame a analizar.
    verbose:
        Si es ``True`` (por defecto) imprime el reporte.

    Returns
    -------
    pandas.DataFrame
        Una fila por columna que tenga al menos un valor faltante,
        ordenada de mayor a menor, con las columnas ``missing`` (conteo) y
        ``percent`` (porcentaje sobre el total de filas).
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("missing() espera un pandas.DataFrame")

    total = len(df)
    counts = df.isna().sum()
    percents = (counts / total * 100).round(2) if total else counts * 0

    result = pd.DataFrame({"missing": counts, "percent": percents})
    result = result[result["missing"] > 0].sort_values("missing", ascending=False)

    if verbose:
        if result.empty:
            print("No hay valores faltantes. 🎉")
        else:
            print(f"Valores faltantes ({total} filas en total):")
            print("-" * 40)
            print(result.to_string())

    return result

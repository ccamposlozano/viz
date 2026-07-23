"""simple_eda: un paquete diminuto para análisis exploratorio de datos (EDA).

Uso rápido:

    import pandas as pd
    import simple_eda as eda

    df = pd.read_csv("data.csv")
    eda.summarize(df)
    eda.missing(df)
"""

from .core import summarize, missing

__version__ = "0.1.0"
__all__ = ["summarize", "missing"]

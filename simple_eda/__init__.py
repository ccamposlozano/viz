"""simple_eda: un paquete diminuto para análisis exploratorio de datos (EDA).

Uso rápido:

    import pandas as pd
    import simple_eda as eda

    df = pd.read_csv("data.csv")
    eda.summarize(df)
    eda.missing(df)

    import matplotlib.pyplot as plt
    eda.histograms(df)
    eda.boxplots(df)
    plt.show()
"""

from .core import summarize, missing
from .plots import histograms, boxplots

__version__ = "0.2.0"
__all__ = ["summarize", "missing", "histograms", "boxplots"]

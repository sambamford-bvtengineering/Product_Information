import pandas as pd
from . import data
import importlib.resources


def autex_frontier_acoustic_fins():
    """Return a dataframe containing Autex frontier acoustic fin data"""

    path = importlib.resources.open_text(data, "Autex Frontier Acoustic Fins.csv")

    return pd.read_csv(path)

def tracklok():
    """Return a dataframe containing tracklok data"""

    path = importlib.resources.open_text(data, "tracklok.csv")

    return pd.read_csv(path)

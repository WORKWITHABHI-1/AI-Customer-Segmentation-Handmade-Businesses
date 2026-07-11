import pandas as pd

def load_data(path):
    """
    Load customer dataset
    """
    return pd.read_csv(path)
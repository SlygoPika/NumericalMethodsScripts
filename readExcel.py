import pandas as pd


def readExcel(name):
    df = pd.read_excel(name)
    return df

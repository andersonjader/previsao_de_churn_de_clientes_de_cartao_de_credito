import os
from pathlib import Path
from pandas import *
import pandas as pd


def catchPath(arq):

    root = Path().resolve().parent
    p = os.path.join(root,arq)
    return p

def SaveDataFrame(df, name):
    """
    This function receives a datafreme as a parameter and the file name and 
    saves the data in an excel spreadsheet in the data directory
    """
    n = 'data/' + name + '.xlsx'
    p = catchPath(n)
    df.to_excel(p, index = False)

def make_dataframe(serie, nome, nome_novo):
    """
    função que cria um dataframe a partir de uma serie que foi gerada de um slice de uma lina
    recebe como parametro: a serie, o nome da coluna atual e depois o nome novo nome
    """

    d = pd.DataFrame(serie)
    d = d.rename(columns={nome:nome_novo})
    d = d.transpose()
    return d

def concat_dataframes(frames):
    d = pd.concat(frames)
    return d
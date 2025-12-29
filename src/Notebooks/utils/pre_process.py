import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from imblearn.under_sampling import RandomUnderSampler


import matplotlib.pyplot as plt
import seaborn as sns

def norm_Data(df,col):
  """
  function that normalizes the data and returns a dataframe
  parameters: df: dataframe, col: selected columns
  """
  df_norm = StandardScaler().fit_transform(df[col])
  df2 = pd.DataFrame(data=df_norm, columns=col)
  return df2

def correlation(df):
  df2 = df.corr().style.background_gradient(cmap='Blues')
  return df2

def correlation_map(df, path_save):
  fig, ax = plt.subplots(figsize=(12,8))
  sns.heatmap(df.corr(), cmap='Blues', linewidths= 0.5, annot=True)
  #plt.savefig(path_save,dpi = 300)

def calc_outliers(dataframe, col):
  q1 = dataframe[col].quantile(0.25)
  q3 = dataframe[col].quantile(0.75)
  FIQ = q3 - q1
  f_baixo = q1 - 1.5*FIQ
  f_alta = q3 - 1.5*FIQ
  f1 = dataframe[col] > f_alta
  f2 = dataframe[col] < f_baixo
  d_alto = dataframe[f1]
  d_baixo = dataframe[f2]
  t_a = d_alto[col].count()
  t_b = d_baixo[col].count()
  return t_a, t_b

def make_boxplot(df,col, caminho):
  sns.boxplot(data=df[col], orient='h',color="#bdd1de", medianprops={"color": "#f0a818"}).set_title(col)
  #plt.savefig(caminho,dpi = 300)

def balances_categories(X, y):
  """
  método que faz uma subamostragem aleatoria de uma população
  com o objetivo de balancear as classes, método é usado apenas para o caso de classes binarias

  recebe como paramentro X: dataframe
  y variavel categorica
  """
  rus = RandomUnderSampler(random_state=0)
  X_resampled, y_resampled = rus.fit_resample(X, y)
  return X_resampled, y_resampled 

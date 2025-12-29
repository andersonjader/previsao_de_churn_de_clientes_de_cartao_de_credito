import pandas as pd
from scipy import stats
from scipy.stats import anderson
from scipy.stats import wilcoxon

import matplotlib.pyplot as plt
import seaborn as sns

def QQplot(data):
    fig, ax = plt.subplots()
    stats.probplot(data, fit=True,   plot=ax)
    plt.title('QQplot')
    plt.show()

def calcShapiro(data):
    r = stats.shapiro(data)
    return r[1]

def cal_Anderson_Darling(data,a):

    """
    metodo que calcula o teste Anderson-Darling
    recebe como paramentro data: dado a ser testado 
    e a: alfa

    e retorna o resultado se passou no teste
    """
    p = anderson(data).statistic
    if p < a:
        r = 'non-standard distribution'
        return r
    else:
        r = 'standard distribution'
        return r

def dagostinho(data,a):
    """
    metodo que calcula o teste d'Agostinho K^2
    recebe como paramentro data: dado a ser testado 
    e a: alfa

    e retorna o resultado se passou no teste
    """
    _, p = stats.normaltest(data)
    if p < a:
        r = 'non-standard distribution'
        return r
    else:
        r = 'standard distribution'
        return r

def test_hipotesis_Wilcoxon(data1,data2,a):

    """
    Teste não paramétrico: Wilcoxon
    recebe como paramentro um par de dados data1,data2 : dado a comparado 
    e a: alfa

    e retorna o resultado se passou no teste
    """

    _, p = wilcoxon(data1,data2)

    if p < a:
        r = "there is a significant difference"
        return r, p
    else:
        r = 'there is no significant difference'
        return r, p

def distribuitionGaus(data, name):
    #densidade, método kdeplot para densidade
    sns.kdeplot(data, color='blue').set(title=name)
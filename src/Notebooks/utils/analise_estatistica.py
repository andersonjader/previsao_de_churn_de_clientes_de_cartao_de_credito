import pandas as pd
from scipy import stats
from utils.general import catchPath

from scipy.stats import mannwhitneyu

import matplotlib.pyplot as plt
import seaborn as sns

def analise_pareada(df, variavel, grupo="Status_Cliente"):
    
    grupo1 = df[df[grupo] == "Cliente Ativo"][variavel]
    grupo2 = df[df[grupo] == "Cliente Cancelado"][variavel]
    
    # Medianas
    mediana_ativo = grupo1.median()
    mediana_cancelado = grupo2.median()
    
    # Teste Mann–Whitney
    stat, p = mannwhitneyu(grupo1, grupo2)
    
    # Tamanho de efeito (rank-biserial)
    n1 = len(grupo1)
    n2 = len(grupo2)
    r = 1 - (2 * stat) / (n1 * n2)
    
    return {
        "Variavel": variavel,
        "Mediana_Ativo": mediana_ativo,
        "Mediana_Cancelado": mediana_cancelado,
        "U": stat,
        "p_valor": p,
        "r": r
    }   
def calculaMediana(df, variavel):
    mediana = df.groupby("Status_Cliente")[variavel].median().reset_index()
    return mediana

def makeplotbox(df, titulo_arq, titulo_graf, variavel, yrotulo):
    """
    função que faz o boxplot padronizado, recebe como parametros:
    df = dataframe
    titulo_arq = nome do arquivo para salvar a imagem
    titulo_graf = titulo do gráfico
    variavel = a variavel a ser analisada
    yrotulo =  rotulo do exo y
    """
    
    #import matplotlib.pyplot as plt
    #import seaborn as sns

    
    cores_status = ["#219ebc", "#023047"]
    
    plt.figure(figsize=(12, 6))
    
    sns.boxplot(
        data=df, 
        x="Status_Cliente", 
        y=variavel,
        hue="Status_Cliente",     
        palette=cores_status,      
        legend=False               
    )
    
    
    plt.title(titulo_graf, fontsize=16)
    plt.xlabel("Status do Cliente", fontsize=12)
    plt.ylabel(yrotulo, fontsize=12)
    
    
    n = catchPath(f'image/{titulo_arq}.png')
    plt.savefig(n, dpi=300, bbox_inches='tight')
    plt.show()


def makeBarPlot(df, variavel, titulo_graf, titulo_arq):
    #import seaborn as sns
    #import matplotlib.pyplot as plt
    
    m = calculaMediana(df,variavel)

    minha_paleta = ['#219ebc', '#023047']
    
    plt.figure(figsize=(8, 5))
    
    sns.barplot(
        data=m, 
        x="Status_Cliente", 
        y=variavel,
        hue="Status_Cliente", 
        palette=minha_paleta,
        legend=False
    )
    
    plt.title(f"Mediana de {titulo_graf}")
    plt.tight_layout()
    n = catchPath(f'image/{titulo_arq}.png')
    plt.savefig(n, dpi=300, bbox_inches='tight')
    plt.show()
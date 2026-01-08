import pandas as pd
from scipy import stats
import numpy as np

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

    import pandas as pd


def calcular_confianca_amostral(N, n, e=0.05):
    """
    Calcula o nível de confiança estatística de uma amostra em uma população finita.
    
    Parâmetros:
    N (int): Tamanho total da população.
    n (int): Tamanho da amostra utilizada.
    e (float): Margem de erro (padrão 0.05 para 5%).
    
    Retorna:
    pd.DataFrame: Tabela com os parâmetros calculados.
    """
    p = 0.5  # Máxima variabilidade (cenário conservador)
    
    # 1. Cálculo do Escore-Z invertendo a fórmula da amostra finita
    # Z = sqrt( (n * e^2 * (N-1)) / (p * (1-p) * (N-n)) )
    numerador = n * (e**2) * (N - 1)
    denominador = p * (1 - p) * (N - n)
    z_calculado = np.sqrt(numerador / denominador)
    
    # 2. Cálculo do Nível de Confiança baseado no Z (Distribuição Normal)
    # stats.norm.cdf(z) nos dá a área à esquerda; transformamos para o intervalo central
    confianca = (2 * stats.norm.cdf(z_calculado) - 1) * 100
    
    # 3. Formatação dos dados para o DataFrame
    percentual_amostra = (n / N) * 100
    
    df_resultado = pd.DataFrame({
        "Parâmetro": [
            "População Total (N)",
            "Tamanho da Amostra (n)",
            "Margem de Erro (e)",
            "Escore-Z calculado",
            "Nível de Confiança"
        ],
        "Valor": [
            f"{N:,}".replace(",", "."),
            f"{n:,} ({percentual_amostra:.1f}%)".replace(",", "."),
            f"{e*100:.1f}%",
            f"{z_calculado:.2f}",
            f"{confianca:.1f}%"
        ]
    })
    
    return df_resultado

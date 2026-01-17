# 📊 Previsão de Churn de Clientes de Cartão de Crédito

## 📌 Visão Geral

Este projeto tem como objetivo analisar e prever o **churn (cancelamento)** de clientes de cartão de crédito a partir de dados comportamentais e financeiros.  
A abordagem adotada vai além da simples construção de modelos preditivos, incorporando **análise exploratória aprofundada**, **estatística descritiva e inferencial** e **seleção criteriosa de variáveis**, seguindo boas práticas de Ciência de Dados.

O dataset utilizado é público e foi obtido no Kaggle:

> Credit Card Customers Dataset

---

## 🐳 Ambiente de Desenvolvimento (Docker)
Para garantir a reprodutibilidade total, o projeto foi desenvolvido utilizando a seguinte imagem Docker:
**Imagem:** `andersonbrizola/machinelearninggeral:v1.2`

<pre>
	docker pull andersonbrizola/machinelearninggeral:v1.2
</pre>
<pre>
	docker run -p 8888:8888 andersonbrizola/machinelearninggeral:v1.2
</pre>

## 🎯 Objetivos do Projeto

- Compreender o comportamento de clientes ativos e cancelados
- Identificar variáveis com **diferenças estatisticamente significativas** entre os grupos
- Selecionar features com base em **estatística, correlação e métodos automáticos**
- Construir um modelo de Machine Learning para previsão de churn
- Garantir reprodutibilidade e evitar vazamento de dados

---

## 🗂️ Estrutura do Repositório

previsao_de_churn_de_clientes_de_cartao_de_credito/
│
├── data/
│ └── dados_tratados.csv
│
├── images/
│ └── visualizacoes_eda/
│
├── notebooks/
│ ├── EDA.ipynb
│ ├── Modelagem.ipynb
│ └── utils/
│ └── funcoes_estatisticas.py
│
├── models/
│ └── pipeline_final.joblib
│
└── README.md


---

## 🧪 Metodologia

### 1️⃣ Análise Exploratória de Dados (EDA)

- Inspeção inicial do dataset
- Identificação de variáveis numéricas e categóricas
- Análise da variável alvo (*Cliente Ativo* vs *Cliente Cancelado*)
- Estudo das distribuições, presença de outliers e assimetria

**Resultado da EDA:**  
As variáveis numéricas apresentam **distribuições assimétricas e outliers**, indicando que métricas como média e testes paramétricos não seriam adequados.

---

### 2️⃣ Análise Estatística Descritiva e Inferencial

Para comparar clientes ativos e cancelados, foi adotada uma **análise pareada robusta**, composta por:

- Medida de tendência central: **mediana**
- Teste estatístico: **Mann–Whitney U**
- Avaliação de:
  - p-valor (significância estatística)
  - tamanho de efeito (r)

#### Variáveis analisadas:
- Quantidade_Transacoes
- Valor_Total_Transacoes
- Meses_Inativos_12m
- Taxa_Utilizacao_Credito
- Limite_Credito
- Idade

#### Principais resultados:

| Variável                  | Diferença Significativa | Tamanho de Efeito |
|---------------------------|-------------------------|-------------------|
| Quantidade_Transacoes     | Sim                     | Forte             |
| Valor_Total_Transacoes    | Sim                     | Moderado          |
| Meses_Inativos_12m        | Sim                     | Moderado          |
| Taxa_Utilizacao_Credito   | Sim                     | Moderado          |
| Limite_Credito            | Sim                     | Fraco             |
| Idade                     | Não                     | Irrelevante       |

A variável **Idade** não apresentou diferença estatisticamente significativa entre os grupos e foi considerada pouco informativa isoladamente.

---

### 3️⃣ Análise de Correlação

- Método utilizado: **Spearman**
- Motivo: adequado para dados não normais
- Objetivo:
  - Identificar multicolinearidade
  - Evitar redundância entre variáveis

Variáveis altamente correlacionadas foram consideradas com cautela na etapa de seleção de features.

---

### 4️⃣ Seleção de Variáveis (Feature Selection)

A seleção final foi baseada em uma **abordagem híbrida**, combinando:

- Evidência estatística
- Tamanho de efeito
- Análise de correlação
- Método automático: **SelectFDR (α = 0.05)**

#### Features selecionadas:

[
'Total_Produtos',
'Meses_Inativos_12m',
'Contatos_12m',
'Limite_Credito',
'Saldo_Rotativo',
'Variacao_Valor_Transacoes',
'Valor_Total_Transacoes',
'Quantidade_Transacoes',
'Variacao_Qtd_Transacoes',
'Taxa_Utilizacao_Credito'
]


Essa abordagem garante que as variáveis escolhidas sejam relevantes do ponto de vista estatístico, pouco redundantes e informativas para o modelo.

---

## 🤖 Modelagem Preditiva

- Separação treino/teste realizada antes de qualquer transformação
- Balanceamento aplicado **apenas no conjunto de treino**
- Construção de pipeline contendo:
  - Pré-processamento
  - Modelo de classificação
- Avaliação com métricas adequadas ao problema de churn

O pipeline final foi salvo para garantir **reprodutibilidade**.

---
### Calibração Estratégica (Threshold Tuning)
Diferente de modelos padrão, ajustamos o limiar de decisão para **0.65**. Esta escolha prioriza a **Especificidade**, garantindo que o modelo seja altamente sensível ao Churn, reduzindo em 36% o risco de perda de clientes não detectados.


## 📈 Principais Insights

- Clientes que cancelam realizam significativamente menos transações
- Maior inatividade nos últimos meses aumenta o risco de churn
- Variáveis comportamentais são mais relevantes do que variáveis demográficas
- Nem toda significância estatística implica grande impacto prático, reforçando a importância do tamanho de efeito

---

## 📈 Resultados e Performance do Modelo

Após a etapa de modelagem, o algoritmo **Random Forest** foi selecionado por apresentar a melhor capacidade de generalização. O diferencial deste projeto foi a **Calibração de Limiar (Threshold Tuning)**: ajustamos o corte de decisão para **0.65**, priorizando a segurança operacional e a retenção de clientes.

### Comparativo Operacional
Abaixo, os resultados obtidos no conjunto de teste final, destacando como o modelo se comporta na detecção real de Churn:

| Métrica | Resultado | Impacto de Negócio |
| :--- | :---: | :--- |
| **Especificidade (Churn)** | **89.2%** | Identifica quase 9 em cada 10 clientes que pretendem cancelar o serviço. |
| **Sensibilidade (Ativos)** | **75.0%** | Mantém a precisão em clientes saudáveis, evitando custos excessivos de retenção. |
| **AUC-ROC** | **0.91** | Indica uma altíssima qualidade de separação entre as classes. |
| **Acurácia Global** | **77.3%** | Reflete o equilíbrio estratégico voltado para a proteção da base de dados. |

> **Nota Técnica:** A escolha pelo aumento da Especificidade (de ~83% para 89%) permitiu reduzir em **36%** o número de "fugas cegas" (clientes que saem sem que o modelo emita um alerta), otimizando o planejamento preventivo da empresa.

### 🚀 Entrega para Produção
O projeto inclui um **Motor de Decisão** que converte as probabilidades do modelo em ações práticas (Ex: Score > 85% = Contato Humano Imediato), gerando listas de prioridade para as equipas de CRM.


## 🧠 Tecnologias Utilizadas

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- SciPy, Scikit-learn  
- Jupyter Notebook  
- Docker

---

## 👤 Autor

**Anderson Jader**  
Ciência de Dados | Estatística | Machine Learning


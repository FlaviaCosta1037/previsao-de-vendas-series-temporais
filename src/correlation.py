import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heatmap_correlacao(df):
    """
    Gera Heatmap apenas com colunas numéricas relevantes.
    """

    colunas_renomeadas = [
        'Units', 'Revenue USD', 'Commission USD', 'Cambio', 'GM',
        'EBIT', 'Revenue BRL', 'GM BRL', 'EBIT BRL', 'Receita USD',
        'Receita BRL', 'Custo USD', 'Custo BRL'
    ]

    # Apenas as colunas que existem
    colunas_existentes = [col for col in colunas_renomeadas if col in df.columns]

    # Filtra e converte para numérico, erros viram NaN
    df_filtrado = df[colunas_existentes].apply(pd.to_numeric, errors='coerce')

    # Gera o Heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_filtrado.corr(), annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Heatmap de Correlação - Variáveis Numéricas')
    plt.show()

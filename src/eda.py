import matplotlib.pyplot as plt
import seaborn as sns

def plot_evolucao_vendas(df):
    plt.figure(figsize=(10,6))
    sns.lineplot(x=df['Data'], y=df['Units'])
    plt.title('Evolução Temporal de Vendas')
    plt.xlabel('Tempo (Mês/Ano)')
    plt.ylabel('Unidades Vendidas')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()  

    # Histograma de distribuição de vendas
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Units'], kde=True)
    plt.title(f'Distribuição de vendas')
    plt.ylabel('Frequência')
    plt.show()
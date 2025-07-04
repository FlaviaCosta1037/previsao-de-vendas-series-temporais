import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Estilo mais elegante
sns.set_theme(style="whitegrid")

def plot_evolucao_vendas(df):
    plt.figure(figsize=(12, 7))
    # Linha mais suave com gradiente azul
    sns.lineplot(x=df['Data'], y=df['Units'], color="#007acc", linewidth=2.5, marker='o')
    
    plt.title('📈 Evolução Temporal de Vendas', fontsize=16, fontweight='bold')
    plt.ylabel('Unidades Vendidas', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.xticks(rotation=45)
    
    # Formato automático das datas
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    
    plt.tight_layout()
    plt.show()

    # Histograma de distribuição de vendas
    plt.figure(figsize=(12, 7))
    sns.histplot(df['Units'], kde=True, color="#009688", bins=30, edgecolor='black', alpha=0.7)
    
    plt.title('📊 Distribuição das Vendas', fontsize=16, fontweight='bold')
    plt.xlabel('Unidades Vendidas', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
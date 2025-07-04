from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns

# Mantém o padrão visual geral
sns.set_theme(style="whitegrid")

def decompor_serie(serie, freq=12):
    result = seasonal_decompose(serie, model='additive', period=freq)
    
    plt.figure(figsize=(14, 10))
    fig = result.plot()
    
    # Deixa o gráfico mais espaçado
    fig.set_size_inches(14, 10)
    fig.suptitle('🔎 Decomposição Sazonal da Série Temporal', fontsize=18, fontweight='bold')

    # Aplica grid discreto em todos subplots
    for ax in fig.axes:
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Espaço pro título não ficar cortado
    plt.show()


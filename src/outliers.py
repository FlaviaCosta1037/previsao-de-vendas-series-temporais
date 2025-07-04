import seaborn as sns
import matplotlib.pyplot as plt

def detectar_outliers(df, coluna):
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1
    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr
    outliers = df[(df[coluna] < limite_inf) | (df[coluna] > limite_sup)]
    return outliers, limite_inf, limite_sup


def plot_outliers(df, coluna, limite_inf, limite_sup):
    plt.figure(figsize=(12, 7))
    
    # Caixa mais estilizada
    sns.boxplot(data=df, x=coluna, color='#42a5f5', linewidth=2, fliersize=5)
    
    plt.axvline(limite_inf, color='red', linestyle='--', label='Limite Inferior')
    plt.axvline(limite_sup, color='red', linestyle='--', label='Limite Superior')
    
    plt.title(f'🚨 Detecção de Outliers - {coluna}', fontsize=16, fontweight='bold')
    plt.xlabel(coluna, fontsize=12)
    
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

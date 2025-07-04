from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from matplotlib import pyplot as plt
import seaborn as sns

def autocorrelacionar(df_agrupado):
    # Número máximo de lags permitido
    max_lags = df_agrupado.shape[0] // 2
    max_lags
    
    # Garante que o valor usado de lags não ultrapasse o permitido
    lags = min(50, max_lags)

    # Plot ACF e PACF corrigido
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    plot_acf(df_agrupado['Units'], lags=lags, ax=axes[0])
    axes[0].set_title('Autocorrelação (ACF)')
    plot_pacf(df_agrupado['Units'], lags=lags, ax=axes[1])
    axes[1].set_title('Autocorrelação Parcial (PACF)')
    plt.tight_layout()
    plt.show()
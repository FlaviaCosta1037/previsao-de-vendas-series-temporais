from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def decompor_serie(serie, freq=12):
    result = seasonal_decompose(serie, model='additive', period=freq)
    plt.figure(figsize=(12, 8))
    fig = result.plot()
    fig.suptitle('Decomposição Sazonal', fontsize=16)
    plt.tight_layout()
    plt.show()


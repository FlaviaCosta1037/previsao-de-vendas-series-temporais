from statsmodels.tsa.stattools import adfuller

def testar_adf_pacf(df_agrupado):
    resultado_adf = adfuller(df_agrupado['Units'])
    print('Estatística ADF:', resultado_adf[0])
    print('p-valor:', resultado_adf[1])
    print('Usou:', resultado_adf[2], 'lags')
    print('Número de observações:', resultado_adf[3])
    print('\nValores Críticos:')
    for chave, valor in resultado_adf[4].items():
        print(f'   {chave}: {valor:.4f}')

    if resultado_adf[1] <= 0.05:
        print('\n** A série é estacionária (rejeita H0) **')
    else:
        print('\n** A série NÃO é estacionária (não rejeita H0) **')
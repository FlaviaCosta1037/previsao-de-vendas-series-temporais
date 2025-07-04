import pandas as pd

def agrupar_serie(df):
    df_agrupado = df[['Units', 'Commission USD']].groupby(pd.Grouper(freq='MS')).agg({
    'Units': 'sum',
    'Commission USD': 'sum'
}).reset_index()
    print('Tamanho do agrupamento: ',df_agrupado.shape)
    print(df_agrupado.head())
    
    return df_agrupado
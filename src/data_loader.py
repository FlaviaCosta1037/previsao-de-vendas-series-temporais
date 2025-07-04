import pandas as pd

def carregar_dados(caminho):
    df = pd.read_excel(caminho)
    df.rename(columns=lambda x: x.strip(), inplace=True)

    df = df[df['Type'] == 'ACT']
    df = df[df['Business Unit'] == 'Dispenser']
    df = df[df['Region2'] == 'Domestic']
    df = df[df['Units'] > 0]
    df.dropna(subset=['Units', 'Commission USD'], inplace=True)

    df['Data'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month#'].astype(str) + '-01')
    df.set_index('Data', inplace=True)
    return df

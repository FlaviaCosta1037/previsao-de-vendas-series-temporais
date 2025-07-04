import pandas as pd

def tratar_dados(df):
    """
    Função que realiza todo o pré-processamento e limpeza necessários:
    - Remove espaços dos nomes das colunas
    - Filtra apenas registros de Dispensers, Região Doméstica e tipo ACT
    - Remove nulos nas colunas críticas
    - Mantém apenas vendas (Units > 0)
    - Cria a coluna de data corretamente
    - Renomeia colunas econômicas
    - Retorna o DataFrame tratado pronto para análise
    """
    # Remove espaços dos nomes das colunas
    df.rename(columns=lambda x: x.strip(), inplace=True)

    # Filtros principais
    df = df[df['Type'] == 'ACT']  
    df = df[df['Business Unit'] == 'Dispenser']
    df = df[df['Region2'] == 'Domestic']

    # Remove nulos nas colunas importantes
    df.dropna(subset=['Units', 'Commission USD'], inplace=True)

    # Mantém apenas vendas positivas
    df = df[df['Units'] > 0]

    # Criação da coluna de data
    df['Data'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month#'].astype(str) + '-01')
    df.set_index('Data', inplace=True)

    # Renomeia colunas para análise
    df.rename(columns={
        'FX': 'Cambio',
        'Revenue Dispenser': 'Receita USD',
        'Revenue Dispenser BRL': 'Receita BRL',
        'Cost Dispenser': 'Custo USD',
        'Cost Dispenser BRL': 'Custo BRL'
    }, inplace=True)

    return df

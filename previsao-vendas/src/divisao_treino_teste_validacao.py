def dividir_modelagem(df_agrupado):
    
    train_size = int(len(df_agrupado)*0.6)
    val_size = int(len(df_agrupado)*0.2)

    treino = df_agrupado.iloc[:train_size]
    validacao = df_agrupado.iloc[train_size:train_size+val_size]
    teste = df_agrupado.iloc[train_size+val_size:]

    # Variáveis
    y_train = treino['Units']
    y_val = validacao['Units']
    y_test = teste['Units']

    print(f"Tamanho Treino: {len(y_train)}, Validação: {len(y_val)}, Teste: {len(y_test)}")
    
    return y_train, y_val, y_test

def dividir_exog(df_exog):
    """
    Divide a variável exógena entre treino, validação e teste.
    Recebe um DataFrame com apenas a coluna da exógena tratada.
    """
    train_size = int(len(df_exog) * 0.6)
    val_size = int(len(df_exog) * 0.2)

    treino = df_exog.iloc[:train_size]
    validacao = df_exog.iloc[train_size:train_size + val_size]
    teste = df_exog.iloc[train_size + val_size:]

    return treino.squeeze().values, validacao.squeeze().values, teste.squeeze().values

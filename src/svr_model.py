import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error

warnings.filterwarnings('ignore')

# Função MAPE
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Normalização inversa
def denorm(x, maxData, minData):
    return x * (maxData - minData) + minData


def modelar_svr(df_agrupado, exog_col=None, stepahead=3, dimension=12, C=100.0, epsilon=0.01, gamma=0.001):
    """
    Modelo SVR com ou sem variável exógena
    
    Parâmetros:
    - df_agrupado: DataFrame com dados
    - exog_col: nome da coluna exógena ou None
    - stepahead: número de passos futuros para prever
    - dimension: tamanho da janela
    - C, epsilon, gamma: parâmetros do SVR
    """
    
    dataset = df_agrupado['Units'].values
    trainSplit = 0.6
    validSplit = 0.2

    trainSize = int(np.floor(trainSplit * len(dataset)))
    validSize = int(np.floor(validSplit * len(dataset)))
    testSize = len(dataset) - trainSize - validSize

    # Normalização target
    maxData = np.max(dataset)
    minData = np.min(dataset)
    ndataset = (dataset - minData) / (maxData - minData)
    datasetSeries = pd.Series(ndataset)

    # Criação das janelas
    datasetShifted = pd.concat([datasetSeries.shift(i) for i in range(dimension + stepahead)], axis=1)

    # Exógena, se existir
    if exog_col:
        exog = df_agrupado[exog_col].values
        maxExog = np.max(exog)
        minExog = np.min(exog)
        nexog = (exog - minExog) / (maxExog - minExog)
        exogSeries = pd.Series(nexog)
        exogShifted = pd.concat([exogSeries.shift(i) for i in range(dimension + stepahead)], axis=1)

    # Loop dos passos futuros
    for i in range(stepahead):
        
        Target = datasetShifted.iloc[dimension + (stepahead - 1):, -(dimension + i + 1)]
        
        # Inputs
        Input_units = datasetShifted.iloc[dimension + (stepahead - 1):, -dimension:]

        if exog_col:
            Input_exog = exogShifted.iloc[dimension + (stepahead - 1):, -dimension:]
            Input = pd.concat([Input_units.reset_index(drop=True), Input_exog.reset_index(drop=True)], axis=1)
        else:
            Input = Input_units

        # Divisão
        Input_train = Input.iloc[:trainSize]
        Input_valid = Input.iloc[trainSize:trainSize + validSize]
        Input_test = Input.iloc[trainSize + validSize:]

        Target_train = Target.iloc[:trainSize]
        Target_valid = Target.iloc[trainSize:trainSize + validSize]
        Target_test = Target.iloc[trainSize + validSize:]

        print(f"\n--- Previsão SVR - Passo {i+1} ---")

        # Modelo SVR
        mySVR = SVR(C=np.float64(C), epsilon=np.float64(epsilon), gamma=np.float64(gamma))
        mySVR.fit(Input_train, Target_train)

        # Previsões
        pred_train = mySVR.predict(Input_train)
        pred_valid = mySVR.predict(Input_valid)
        pred_test = mySVR.predict(Input_test)

        # Inversão da normalização
        y_train_real = denorm(Target_train, maxData, minData)
        y_valid_real = denorm(Target_valid, maxData, minData)
        y_test_real = denorm(Target_test, maxData, minData)

        pred_train_real = denorm(pred_train, maxData, minData)
        pred_valid_real = denorm(pred_valid, maxData, minData)
        pred_test_real = denorm(pred_test, maxData, minData)

        # Métricas
        print(f"Treino - MAE: {mean_absolute_error(y_train_real, pred_train_real):.2f}, "
              f"MSE: {mean_squared_error(y_train_real, pred_train_real):.2f}, "
              f"MAPE: {mape(y_train_real, pred_train_real):.2f}%")
        
        print(f"Validação - MAE: {mean_absolute_error(y_valid_real, pred_valid_real):.2f}, "
              f"MSE: {mean_squared_error(y_valid_real, pred_valid_real):.2f}, "
              f"MAPE: {mape(y_valid_real, pred_valid_real):.2f}%")
        
        print(f"Teste - MAE: {mean_absolute_error(y_test_real, pred_test_real):.2f}, "
              f"MSE: {mean_squared_error(y_test_real, pred_test_real):.2f}, "
              f"MAPE: {mape(y_test_real, pred_test_real):.2f}%")

        # Gráfico Real x Previsto
        plt.figure(figsize=(14, 6))
        plt.title(f'SVR - Previsão - Passo {i+1} {"com Exógena" if exog_col else "sem Exógena"}')

        plt.plot(range(len(y_train_real)), y_train_real, label='Treino Real', color='blue')
        plt.plot(range(len(pred_train_real)), pred_train_real, '--', label='Treino Previsto', color='cyan')

        plt.plot(range(len(y_train_real), len(y_train_real) + len(y_valid_real)), y_valid_real, label='Validação Real', color='green')
        plt.plot(range(len(pred_train_real), len(pred_train_real) + len(pred_valid_real)), pred_valid_real, '--', label='Validação Prevista', color='lime')

        plt.plot(range(len(y_train_real) + len(y_valid_real), len(y_train_real) + len(y_valid_real) + len(y_test_real)), y_test_real, label='Teste Real', color='red')
        plt.plot(range(len(pred_train_real) + len(pred_valid_real), len(pred_train_real) + len(pred_valid_real) + len(pred_test_real)), pred_test_real, '--', label='Teste Previsto', color='orange')

        plt.xlabel('Índice Temporal')
        plt.ylabel('Units')
        plt.grid(True)
        plt.legend()
        plt.show()

        # Última previsão isolada
        last_instance = Input.iloc[-1, :].values
        previsao = mySVR.predict(last_instance.reshape(1, -1))
        previsao_real = denorm(previsao, maxData, minData)

        print("Última previsão isolada:", np.abs(previsao_real))



from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats
from src.divisao_treino_teste_validacao import dividir_exog, dividir_modelagem

def modelar_sarimax(df_agrupado, order=(4,1,4), seasonal_order=(0,0,0,0), auto=True, exog_type='log'):
    """
    Modelagem SARIMAX com variável exógena, usando função de divisão existente.
    
    Parâmetros:
    - df_agrupado: dataframe com 'Units' e exógena
    - order: tupla (p,d,q) do ARIMA
    - seasonal_order: tupla (P,D,Q,s)
    - auto: se True usa auto_arima
    - exog_type: 'log' ou 'scale' para a variável exógena
    """
    df_agrupado = df_agrupado.copy()
    df_agrupado.index = pd.to_datetime(df_agrupado.index)
    
    exog_col = 'Commission USD'
    target_col = 'Units'

    # -------------------
    # Tratamento da exógena
    # -------------------
    if exog_type == 'log':
        df_agrupado['exog_tratada'] = np.log(df_agrupado[exog_col].values)
    elif exog_type == 'scale':
        scaler = StandardScaler()
        df_agrupado['exog_tratada'] = scaler.fit_transform(df_agrupado[exog_col].values.reshape(-1,1)).flatten()
    else:
        raise ValueError("exog_type deve ser 'log' ou 'scale'")

    # -------------------
    # Divisão dos dados
    # -------------------
    y_train, y_val, y_test = dividir_modelagem(df_agrupado)
    exog_train, exog_val, exog_test = dividir_exog(df_agrupado[['exog_tratada']])  
 
    y_train = y_train.values
    y_val = y_val.values
    y_test = y_test.values

    # -------------------
    # Busca automática ou manual
    # -------------------
    if auto:
        stepwise_model = auto_arima(
            y_train, exogenous=exog_train, seasonal=True, m=12, trace=True, suppress_warnings=True
        )
        order = stepwise_model.order
        seasonal_order = stepwise_model.seasonal_order

    print(f"\nParâmetros SARIMAX: Order={order}, Seasonal={seasonal_order}")

    # -------------------
    # Modelo no Treino
    # -------------------
    model = SARIMAX(y_train, exog=exog_train, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False)

    y_val_pred = model_fit.forecast(steps=len(y_val), exog=exog_val)

    # -------------------
    # Avaliação Validação
    # -------------------
    mae_val = mean_absolute_error(y_val, y_val_pred)
    rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
    mape_val = mean_absolute_percentage_error(y_val, y_val_pred) * 100

    print(f"\nVALIDAÇÃO:")
    print(f"MAE  = {mae_val:.2f}")
    print(f"RMSE = {rmse_val:.2f}")
    print(f"MAPE = {mape_val:.2f}%")

    # -------------------
    # Resíduos Treino
    # -------------------
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(model_fit.resid, kde=True)
    plt.title('Histograma Resíduos - Treino')

    plt.subplot(1, 2, 2)
    stats.probplot(model_fit.resid, dist="norm", plot=plt)
    plt.title('QQ-Plot Resíduos - Treino')
    plt.show()

    # -------------------
    # Reajustando com Treino + Validação
    # -------------------
    y_train_val = np.concatenate([y_train, y_val])
    exog_train_val = np.concatenate([exog_train, exog_val])

    model_final = SARIMAX(y_train_val, exog=exog_train_val, order=order, seasonal_order=seasonal_order)
    model_final_fit = model_final.fit(disp=False)

    y_test_pred = model_final_fit.forecast(steps=len(y_test), exog=exog_test)

    # -------------------
    # Avaliação Teste
    # -------------------
    mae_test = mean_absolute_error(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    mape_test = mean_absolute_percentage_error(y_test, y_test_pred) * 100

    print(f"\nTESTE:")
    print(f"MAE  = {mae_test:.2f}")
    print(f"RMSE = {rmse_test:.2f}")
    print(f"MAPE = {mape_test:.2f}%")
    
    # -------------------
    # Análise de Resíduos - Modelo Final (Treino + Validação)
    # -------------------
    residuos_final = model_final_fit.resid

    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(residuos_final, kde=True)
    plt.title('Histograma dos Resíduos - Treino + Validação')

    plt.subplot(1, 2, 2)
    stats.probplot(residuos_final, dist="norm", plot=plt)
    plt.title('QQ-Plot dos Resíduos - Treino + Validação')
    plt.show()

    # -------------------
    # Plot Final Previsões
    # -------------------
    index = df_agrupado.index
    train_size = int(len(df_agrupado)*0.6)
    val_size = int(len(df_agrupado)*0.2)
    val_index = index[train_size:train_size+val_size]
    test_index = index[train_size+val_size:]

    plt.figure(figsize=(12, 6))
    plt.plot(index, df_agrupado[target_col].values, label='Dados Reais', color='blue')
    plt.plot(val_index, y_val_pred, label='Previsão Validação', color='orange')
    plt.plot(test_index, y_test_pred, label='Previsão Teste', color='red')
    plt.title('SARIMAX - Previsão Treino/Validação/Teste')
    plt.grid(True)
    plt.legend()
    plt.show()

    # -------------------
    # Previsão Próximos 3 Meses
    # -------------------
    y_full = np.concatenate([y_train_val, y_test])
    exog_full = np.concatenate([exog_train_val, exog_test])

    model_full = SARIMAX(y_full, exog=exog_full, order=order, seasonal_order=seasonal_order)
    model_full_fit = model_full.fit(disp=False)

    future_dates = pd.date_range(start=index[-1] + pd.DateOffset(months=1), periods=3, freq='MS')
    exog_future = exog_full[-3:] 

    y_future_pred = model_full_fit.forecast(steps=3, exog=exog_future)

    print(f"Previsão de vendas para os próximos 3 meses: {np.floor(y_future_pred).tolist()}")

    # -------------------
    # Retorno dos Resultados
    # -------------------
    return {
        "order": order,
        "seasonal_order": seasonal_order,
        "mape_val": mape_val,
        "mape_test": mape_test,
        "y_val_pred": y_val_pred,
        "y_test_pred": y_test_pred,
        "y_future_pred": y_future_pred
    }

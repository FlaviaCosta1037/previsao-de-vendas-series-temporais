from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from src.divisao_treino_teste_validacao import dividir_modelagem

import warnings
# Ignorar Warnings
warnings.filterwarnings('ignore')

from pmdarima import auto_arima
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from src.divisao_treino_teste_validacao import dividir_modelagem
import warnings
warnings.filterwarnings('ignore')


def modelar_arima_automatico(df_agrupado):
    """
    Modelagem ARIMA automática com auto_arima.
    """
    # -------------------
    # Divisão dos dados
    # -------------------
    y_train, y_val, y_test = dividir_modelagem(df_agrupado)

    # -------------------
    # Busca automática de parâmetros no treino
    # -------------------
    stepwise_model = auto_arima(
        y_train,
        seasonal=True,
        m=1,
        trace=True,
        suppress_warnings=True,
        stepwise=True
    )

    print(f"\nMelhor ordem encontrada pelo auto_arima: {stepwise_model.order}")

    # -------------------
    # Validação
    # -------------------
    model_fit = stepwise_model.fit(y_train)
    y_val_pred = model_fit.predict(n_periods=len(y_val))

    mae_val = mean_absolute_error(y_val, y_val_pred)
    rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
    mape_val = mean_absolute_percentage_error(y_val, y_val_pred) * 100

    print(f'\nVALIDAÇÃO:')
    print(f'MAE  = {mae_val:.2f}')
    print(f'RMSE = {rmse_val:.2f}')
    print(f'MAPE = {mape_val:.2f}%')

    # -------------------
    # Reajustando com Treino + Validação
    # -------------------
    y_train_val = np.concatenate([y_train, y_val])

    model_final = auto_arima(
        y_train_val,
        seasonal=False,
        m=1,
        trace=True,
        suppress_warnings=True,
        stepwise=True
    )

    print(f"\nMelhor ordem final (Treino + Validação): {model_final.order}")

    model_final_fit = model_final.fit(y_train_val)
    y_test_pred = model_final_fit.predict(n_periods=len(y_test))

    mae_test = mean_absolute_error(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    mape_test = mean_absolute_percentage_error(y_test, y_test_pred) * 100

    print(f'\nTESTE:')
    print(f'MAE  = {mae_test:.2f}')
    print(f'RMSE = {rmse_test:.2f}')
    print(f'MAPE = {mape_test:.2f}%')

    # -------------------
    # Visualização Completa
    # -------------------
    plt.figure(figsize=(14, 6))
    plt.plot(y_train.index, y_train, label='Treino')
    plt.plot(y_val.index, y_val, label='Validação')
    plt.plot(y_val.index, y_val_pred, label='Previsão Validação', linestyle='--')
    plt.plot(y_test.index, y_test, label='Teste Real')
    plt.plot(y_test.index, y_test_pred, label='Previsão Teste', linestyle='--')
    plt.title(f'ARIMA Automático - Ordem Final: {model_final.order}')
    plt.legend()
    plt.grid(True)
    plt.show()

    # -------------------
    # Previsão Futura (próximos 3 meses)
    # -------------------
    y_full = np.concatenate([y_train_val, y_test])

    model_full = auto_arima(
        y_full,
        seasonal=False,
        m=1,
        trace=False,
        suppress_warnings=True,
        stepwise=True
    )

    model_full_fit = model_full.fit(y_full)
    future_pred = model_full_fit.predict(n_periods=3)

    print(f"\nPrevisão dos próximos 3 meses: {np.floor(future_pred).tolist()}")

    # -------------------
    # Retorno Completo
    # -------------------
    return {
        "melhor_ordem": model_final.order,
        "mape_val": mape_val,
        "mape_test": mape_test,
        "y_val_pred": y_val_pred,
        "y_test_pred": y_test_pred,
        "y_future_pred": future_pred
    }


    

from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from src.divisao_treino_teste_validacao import dividir_modelagem


def modelar_arima_manual(df_agrupado, order):
    """
    Modelagem ARIMA manual com ordem definida (p,d,q).
    """
    # -------------------
    # Divisão dos dados
    # -------------------
    y_train, y_val, y_test = dividir_modelagem(df_agrupado)

    # -------------------
    # Validação
    # -------------------
    print(f"\nAjustando ARIMA manual com ordem {order} para Validação...")

    model = ARIMA(y_train, order=order)
    model_fit = model.fit()
    y_val_pred = model_fit.forecast(steps=len(y_val))

    # Avaliação Validação
    mae_val = mean_absolute_error(y_val, y_val_pred)
    rmse_val = np.sqrt(mean_squared_error(y_val, y_val_pred))
    mape_val = mean_absolute_percentage_error(y_val, y_val_pred) * 100

    print(f'\nVALIDAÇÃO:')
    print(f'MAE  = {mae_val:.2f}')
    print(f'RMSE = {rmse_val:.2f}')
    print(f'MAPE = {mape_val:.2f}%')

    # -------------------
    # Reajustando Modelo com Treino + Validação
    # -------------------
    y_train_val = np.concatenate([y_train, y_val])

    print(f"\nAjustando ARIMA manual final com ordem {order} para Teste...")

    model_final = ARIMA(y_train_val, order=order)
    model_final_fit = model_final.fit()
    y_test_pred = model_final_fit.forecast(steps=len(y_test))

    # -------------------
    # Avaliação Teste
    # -------------------
    mae_test = mean_absolute_error(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    mape_test = mean_absolute_percentage_error(y_test, y_test_pred) * 100

    print(f'\nTESTE:')
    print(f'MAE  = {mae_test:.2f}')
    print(f'RMSE = {rmse_test:.2f}')
    print(f'MAPE = {mape_test:.2f}%')

    # -------------------
    # Visualização Completa
    # -------------------
    plt.figure(figsize=(14, 6))
    plt.plot(y_train.index, y_train, label='Treino')
    plt.plot(y_val.index, y_val, label='Validação')
    plt.plot(y_val.index, y_val_pred, label='Previsão Validação', linestyle='--')
    plt.plot(y_test.index, y_test, label='Teste Real')
    plt.plot(y_test.index, y_test_pred, label='Previsão Teste', linestyle='--')
    plt.title(f'ARIMA Manual - Ordem {order}')
    plt.legend()
    plt.grid(True)
    plt.show()

    # -------------------
    # Previsão Futura (próximos 3 meses)
    # -------------------
    y_full = np.concatenate([y_train_val, y_test])

    model_full = ARIMA(y_full, order=order)
    model_full_fit = model_full.fit()
    future_pred = model_full_fit.forecast(steps=3)

    print(f"\nPrevisão dos próximos 3 meses: {np.floor(future_pred).tolist()}")

    # -------------------
    # Retorno Completo
    # -------------------
    return {
        "melhor_ordem": order,
        "mape_val": mape_val,
        "mape_test": mape_test,
        "y_val_pred": y_val_pred,
        "y_test_pred": y_test_pred,
        "y_future_pred": future_pred
    }

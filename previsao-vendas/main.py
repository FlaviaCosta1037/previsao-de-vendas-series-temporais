from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import io

from src.data_clean import tratar_dados
from src.grouped import agrupar_serie# ajuste o path se necessário
from src.sarimax_model import modelar_sarimax  

app = FastAPI()

# Permitir acesso do frontend (ajuste se quiser restringir)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/prever")
async def prever(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".xlsx"):
            return {"erro": "Formato de arquivo não suportado. Use um arquivo .xlsx"}

        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # 1. Tratamento
        df_tratado = tratar_dados(df)

        # 2. Agrupamento mensal
        df_agrupado = agrupar_serie(df_tratado)

        # 3. Converter coluna 'Data' para índice
        df_agrupado['Data'] = pd.to_datetime(df_agrupado['Data'])
        df_agrupado.set_index('Data', inplace=True)

        # 4. Rodar modelo
        resultado = modelar_sarimax(df_agrupado, auto=True, exog_type='log')

        previsao = np.floor(resultado["y_future_pred"]).tolist()

        return {"previsao": previsao}

    except Exception as e:
        return {"erro": str(e)}

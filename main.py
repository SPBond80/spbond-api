from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API de Seguro Garantia online e operacional 🚀"}


# Carregar a tabela Excel
df = pd.read_excel("tabela_seguro.xlsx", header=None)
df.columns = ['Valor Garantia', 'Prazo Dias', 'Custo Seguro']

# Modelo de dados esperado no POST
class CalculoRequest(BaseModel):
    nome: str
    endereco: str
    telefone: str
    cnpj: str
    valor_garantia: float
    prazo_dias: int

@app.post("/calcular")
def calcular_seguro(data: CalculoRequest):
    valor_min = data.valor_garantia * 0.95
    valor_max = data.valor_garantia * 1.05
    prazo_min = data.prazo_dias - 30
    prazo_max = data.prazo_dias + 30

    # Filtra registros dentro da faixa de valor e prazo
    filtro = df[
        (df['Valor Garantia'] >= valor_min) & (df['Valor Garantia'] <= valor_max) &
        (df['Prazo Dias'] >= prazo_min) & (df['Prazo Dias'] <= prazo_max)
    ]

    if filtro.empty:
        raise HTTPException(status_code=404, detail="Nenhum cálculo encontrado para os parâmetros informados.")

    media_custo = round(filtro['Custo Seguro'].mean(), 2)
    mediana_custo = round(filtro['Custo Seguro'].median(), 2)
    quantidade_registros = len(filtro)

    return {
        "nome": data.nome,
        "valor_garantia_informado": data.valor_garantia,
        "prazo_dias_informado": data.prazo_dias,
        "quantidade_registros_encontrados": quantidade_registros,
        "media_custo_seguro": media_custo,
        "mediana_custo_seguro": mediana_custo
    }

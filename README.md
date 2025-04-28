
# API de Cálculo de Seguro Garantia

Esta API foi desenvolvida para calcular o custo de seguros garantia com base em um histórico de dados fornecido em planilha Excel. A API permite calcular o valor médio e a mediana dos custos de seguros para condições semelhantes a partir de parâmetros informados.

## Como funciona

A API recebe via POST as seguintes informações:
- `nome` (string)
- `endereco` (string)
- `telefone` (string)
- `cnpj` (string)
- `valor_garantia` (float)
- `prazo_dias` (int)

Ela então busca no banco de dados (planilha Excel) os registros com:
- Valor da garantia dentro de ±5%
- Prazo dentro de ±30 dias

Calcula e retorna:
- Quantidade de registros encontrados
- Média dos custos de seguro encontrados
- Mediana dos custos de seguro encontrados

## Endpoint

### `POST /calcular`

Exemplo de requisição:

```
curl -X 'POST' 'http://127.0.0.1:8000/calcular' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "nome": "string",
  "endereco": "string",
  "telefone": "string",
  "cnpj": "string",
  "valor_garantia": 150000,
  "prazo_dias": 200
}'
```

Resposta de exemplo:

```
{
  "nome": "string",
  "valor_garantia_informado": 150000,
  "prazo_dias_informado": 200,
  "quantidade_registros_encontrados": 13,
  "media_custo_seguro": 1839.49,
  "mediana_custo_seguro": 1182.14
}
```

## Como rodar a API

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Execute o servidor:
```
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

---

Desenvolvido para facilitar o cálculo de seguros garantia com base em dados históricos.

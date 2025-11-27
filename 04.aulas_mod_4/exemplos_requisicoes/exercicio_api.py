import requests
import json

url = "https://brasilapi.com.br/api/cnpj/v1/"
cnpj = "28523215000106"

url_completa = url + cnpj

print(f"Fazendo uma requisição GET para: {url_completa}")

response = requests.get(url_completa)
response.raise_for_status()
dados = response.json()

print("\n======== Detalhes do CNPJ ========")
print(f"Razão Social: {dados.get('razao_social')}")
print(f"Nome Fantasia: {dados.get('nome_fantasia')}")
print(f"Logradouro: {dados.get('logradouro')}")

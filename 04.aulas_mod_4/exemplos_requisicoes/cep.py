import requests #Biblioteca base para executar requisições.
import json #Formato principal de compartilhamento de dados na web

#comando a ser digitado no terminal para instalação da biblioteca requests: pip install requests
#Lembrando: utilizar ambientes virtuais ajuda a não ter problemas com versionamento e conflitos de bibliotecas.

cep = "24470200"
url_base = "https://brasilapi.com.br/api/cep/v1/"

url_completa = url_base + cep

print(f"Fazendo uma requisição GET para: {url_completa}")

response = requests.get(url_completa)

#Para esse exemplo vamos incrementar nosso processo de trabalho da resposta:
response.raise_for_status() #Irá lançar uma exceção caso a resposta seja 4xx ou 5xx.

#Processando a resposta de json para um dicionário python:
dados = response.json()

print("\n======== Detalhes do endereço ========")
print(f"CEP: {dados.get('cep')}")
print(f"Rua/Logradouro: **{dados.get('street')}**")
print(f"Bairro: {dados.get('neighborhood')}")
print(f"Cidade/Estado: {dados.get('city')} - {dados.get('state')}")
print(f"Serviço Fornecedor: {dados.get('service')}")
print("\n")

#Descomente a linha abaixo para visualizar a saída completa do json reportado:

#print(json.dumps(dados))

#Ao visualizar o json em seu formato original, conseguiu notar algo de diferente de como foi feita a exibição anterior?
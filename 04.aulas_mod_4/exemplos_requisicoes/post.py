import requests
import json
from datetime import datetime

url = "https://jsonplaceholder.typicode.com/posts"

#Dados que simulamos enviar para o servidor (Payload)
novo_artigo = {
    "title": "A Importância das Requisições POST",
    "body": "No desenvolvimento back-end, o POST é essencial para criar novos recursos.",
    "userId": 101 # ID de um usuário fictício
}

print("Fazendo requisição POST (Criação de Artigo) sem API Key...")

#Faz a requisição POST. O parâmetro 'json' cuida da serialização.
resposta_post = requests.post(url, json=novo_artigo)

print(f"Status Code POST: {resposta_post.status_code}")

#Como a resposta positiva de criação do recurso é marcada como 201 para o POST/PUT vamos garantir esse resultado.
#A utilização de Try e except em consultas para apis é recomendada para não correr riscos de quebrar a aplicação caso a api esteja offline.
if resposta_post.status_code == 201:
    dados_criados = resposta_post.json()
    
    print("\nRecurso criado com sucesso! (201 Created)")
    print(f"Título: {dados_criados.get('title')}") #Essa linha verifica se o dados criados lá, coincidem com o que enviamos.
    print(f"ID Atribuído pelo Servidor: **{dados_criados.get('id')}**") #O JSONPlaceholder retorna um ID (simulado) para o recurso criado
else:
    print(f"\n Falha na criação. Resposta do servidor: {resposta_post.text}")
import requests #Biblioteca base para executar requisições.
import json #Formato principal de compartilhamento de dados na web

#comando a ser digitado no terminal para instalação da biblioteca requests: pip install requests
#Lembrando: utilizar ambientes virtuais ajuda a não ter problemas com versionamento e conflitos de bibliotecas.


url = "https://pokeapi.co/api/v2/pokemon/"
nome_pokemon = "snorlax"

#Requisição GET para buscar o pokemon:

url_completa = url + nome_pokemon

print(f"Fazendo uma requisição na url:{url_completa}")

response = requests.get(url_completa) #Essa é a linha que de fato faz a requisição, com o método GET!

#O conteúdo ficará salvo na variável response:

print(response) #Esse print trará o statuscode da resposta.

#A resposta não é apenas o status, ela detém conteúdo, vamos utilizar o método json da própria biblioteca requests para visualizar o conteúdo.

dados_pokemon = response.json() #Ela automaticamente transforma de json para um dicionário Python. São formatos muito semelhantes.
#print(dados_pokemon)
print("\n========Detalhes do pokemon========")
print(f"ID (Pokedex): {dados_pokemon['id']}")
print(f"Nome: {dados_pokemon['name'].capitalize()}")

#Os dados exibidos acima são apenas uma fração do que é possível resgatar com a resposta da API:
#Vamos olhar a resposta com a biblioteca json:

#Retire o comentário da linha abaixo para ver o formato completo (Prepare-se para um output longo!)
# print(json.dumps(dados_pokemon,sort_keys=True, indent=4))


#Note que talvez vocẽ não precise de todos esses dados, como no exemplo, eu apenas peguei a id e o name do pokemon para visualização.

#Caso queira salvar essa resposta para visualização completa, descomente e execute o bloco de código abaixo

# with open("pokemon.json", "w") as f:
#    f.write(json.dumps(dados_pokemon,sort_keys = True, indent = 4))


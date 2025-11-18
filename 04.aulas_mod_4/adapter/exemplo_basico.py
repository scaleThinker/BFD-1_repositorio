#Imagine que temos uma aplicação que recebe dados de uma api em um dicionario:

def chama_api(endereço:str):
    print("Coletando dados da API!\n")
    print("----Acessa o endereço----")
    print("----Coleta os dados----")
    return {1:"Primeiro dado",2:"Segundo dado",3:"Terceiro e tal"}

#Agora imagine que nossa aplicação por algum motivo não consegue lidar com ese formato de dicionários
#Precisamos trabalhar com uma lista.

def processa_dados(conteudo_api:list):
    """Nossa função espera uma lista"""
    print("\n *** Lendo conteúdo da lista ***")
    for i in conteudo_api:
        print("==="*10)
        print(i)
    print("==="*10)

#Para contornar o problema podemos fazer o que? Uma função intermediária que adapta os resultado:

def dic_to_list(conteudo_dict:dict) -> list:
    lista_itens = list(conteudo_dict.items())
    return lista_itens

#Com a função dic_to_list conseguimos traduzir o conteúdo
#Adaptando duas interfaces que não se comunicariam.

conteudo_api = chama_api("www.minhaapi.com/api/id=1")

processa_dados(dic_to_list(conteudo_api))
#Essa chamada deixa claro como o dic_to_list adapta o conteúdo para a função processa dados.

#Esse é o exemplo mais simples possível de adaptadores
#É muito comum quando linguagens diferentes de programação precisam interagir.

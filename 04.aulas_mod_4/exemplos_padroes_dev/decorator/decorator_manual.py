#Decorators são estruturas muito simples de serem entendidas.
#Eles são funções que recebem uma função e retornam outra! (Inception!)

#Neste exemplo vamos implementar manualmente um decorator.

#Função principal que será trabalhada:

def principal():
    #Esta será a função que queremos 'decorar'
    print("**** Lógica Principal ****")


#Agora faremos nossa função que recebe a função principal

def meu_decorator(funcao_principal):
    """
        Esta função é o decorator de fato!
        Ela quem recebe a função principal como argumento!
    """
    print("Neste momento o decorator foi 'construído em volta da função'")

    #Agora vem a mágica, vamos declarar uma função dentro de outra função!
    def wrapper(): #O que significa wrapper? Nesses momentos o conhecimento de língua inglesa pode ajudar! Não deixe de estudar!
        #wrapper == envelope
        
        #Adicionamos uma nova lógica que irá envolver a função principal!
        print("Alguma lógica muito legal executada antes da minha função principal!")

        #Executamos a função principal!
        funcao_principal()

        #Adicionamos uma nova lógica que pode envolver a função principal e ser executada depois, depende da necessidade!

        print("A função terminou de ser executada, e aqui pode conter alguma lógica")


    return wrapper

""" IMPORTANTE!

    Note que o retorno do meu_decorator() é a função wrapper descrita internamente nele!
    Logo, a identação do return precisa estar ligada ao decorator e não ao wrapper!

"""

#Implementando o decorator manualmente!

decorada = meu_decorator(principal) #Estou passando a funcao principal como argumento para o decorador.

#Como o decorator retorna uma nova função, a nossa variável "decorada" se tornará uma função!


#Vamos chamar a função para ver sua saída!
decorada()

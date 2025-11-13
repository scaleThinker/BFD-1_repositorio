#Vamos repetir nossa função de implementação para esse exemplo!

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


#O python utilize o "@" para declarar e chamar decorators.
#Podemos implementar este decorator de forma direta utilizando apenas a seguinte sintaxe:

@meu_decorator
def seg_funcao():
    """Esta função já vai nascer decorada!"""
    print("****Executando a lógica principal****")


seg_funcao() #Como a função foi decorada diretamente utilizando a sintaxe acima, só precisamos chamar!


print(f"\nNome da função: {seg_funcao.__name__}")
print(f"\nDocstring da função: {seg_funcao.__doc__}")


#Neste exemplo estarei criando um decorator para medir o tempo de execução de uma função.

import time
import functools

def log_tempo(func): #Este é vai ser o meu decorator!
    """ Função para medir tempo de execução """ #Docstring pra ficar bonito!
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Docstring que será substituída! Estou colocando apenas como lembrete!"""
        #Aqui vou implementar a lógica que será aplicada a todas as funções
        #que forem decoradas por esse decorator!

        inicio = time.time() #Pego o ínicio do tempo de execução!

        resultado = func(*args, **kwargs) #chamada da função principal!

        total = time.time() - inicio #Meu cálculo do tempo total da execução!

        print(f"O tempo total da execução foi de:{total:.8f}")
        return resultado #Não podemos esquecer do resultado da função principal!

    return wrapper #E o retorno do envelope da noção função para que seja possível decorar!


#Com meu decorator criado, vamos testar!

@log_tempo
def funcao_lenta():
    print("Hackeando a NASA!")
    time.sleep(5)
    print("HaCk3Ad0S")
    return "Fomos presos!"


@log_tempo
def multiplica(x,y):
    print("Multiplicando!!")
    return x * y


#Definidas as funções decoradas, vamos testar!

print(10*"-"+"Teste da função lenta"+10*"-")

resultado = funcao_lenta()
print(resultado+"\n")

print(10*"-"+"Teste da função rápida!"+10*"-")

multiplica(5,10)

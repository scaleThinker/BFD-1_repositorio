# 1 - Crie uma função chamada "gera_lista".
# Essa função deve receber como parâmetro um número inteiro com o total de números que a lista deve conter, e retornar a lista gerada.
# Os números devem ser do tipo inteiro e  gerados aleatoriamente utilizando a biblioteca random.
# Exemplo de chamada: gera_lista(5)
# Exemplo de retorno: [6,25,60,16,5]

import random
def geralista(n:int):
    var=[]
    for i in range(n):
        var.append(random.randint(0,1000))
    return var

# 2 - Crie uma função chamada "analisar_numeros". 
# Essa função deve receber como parâmetro uma lista contendo 200 números gerados a partir da função do exercício 1 e 
# retornar um dicionário contendo as seguintes informações:
# A - O total de números na lista
# B - A quantidade de números pares
# C - A quantidade de números ímpares
# D - A soma de todos os números
# E - A média dos números
# F - Os números primos presentes na lista.

lista = geralista(200)
print(lista)

def analisar_numeros(lista):
    qnt = len(lista)
    
    n_pares = []
    n_impares = []
    for i in lista:
        verificacao = i % 2
        if verificacao == 0:
            n_pares.append(i)
        elif verificacao == 1:
            n_impares.append(i)

    qnt_pares = len(n_pares)
    
    qnt_impares = len(n_impares)
    
    soma = sum(lista)

    media = soma / qnt

    primos = []
    for n in lista:
        n_zeros = []
        for i in range(1, n + 1):
            resto = n/2 % i
            if resto == 0:
                n_zeros.append(i) 
        if len(n_zeros) == 2:
            primos.append(n)
    
    dic = {"Total":qnt,"Pares":qnt_pares,"Ímpares":qnt_impares,"Soma":soma,"Média":media,"Números primos":primos}
    return dic
    

print(analisar_numeros(lista))
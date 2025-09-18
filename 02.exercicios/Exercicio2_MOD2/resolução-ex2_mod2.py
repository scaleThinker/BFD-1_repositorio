# 1 - Crie uma função chamada "gera_lista".
# Essa função deve receber como parâmetro um número inteiro com o total de números que a lista deve conter, e retornar a lista gerada.
# Os números devem ser do tipo inteiro e  gerados aleatoriamente utilizando a biblioteca random.
# Exemplo de chamada: gera_lista(5)
# Exemplo de retorno: [6,25,60,16,5]

import random
def geralista (n:int):
    var = []
    for i in range (n):
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

lista = geralista(5)
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

    def num_primos (lista):
        primos = []
        n_zeros = []
        for i in range (qnt):
            resto = qnt % 2
            if resto == 0:
                n_zeros.append(i)
        if len


analisar_numeros(lista)

"""
n = 4
n_primos = []
while True:
    acumulador = []
    for i in range(n):
        contagem = i+1 #deixa o range de 1 a n
        ver_primo = n % 2contagem #se as divisões tiverem dois 0, é primo
        if ver_primo == 0:
            acumulador.append(i)
    if len(acumulador) == 2:
        n_primos.append(n)
"""

# n = 4
# for i in range(n):
#         contagem = i+1 #deixa o range de 1 a n
#         ver_primo = n % 2
#         print (ver_primo)


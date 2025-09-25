from random import randint
import cProfile

def gera_lista(ini,fim,total):
    result = []
    for _ in range(total): # o _ é uma forma de dizer que não irei utilizar o valor encontrado a cada passo (apenas escolha estética, não muda nada)
        result.append(randint(ini,fim))
    return result

n_ran = gera_lista(1,10000000,200)


def calc_primo(n): #Cálculo mais simples possível.
    divs = []
    for i in range(1,n):
        if n % (i) == 0:
            divs.append(i)
    if len(divs) > 1:
        return False
    else:
        return True

def calc_primo_metade(n): #Cálculo até a metade do caminho
    divs = []
    for i in range(1,n//2):
        if n % i == 0:
            divs.append(i)
    if len(divs) > 1:
        return False
    else:
        return True

def calc_primo_raiz(n): #Cálculo até a raiz
    divs = []
    for i in range(1,int(n**1/2)+1):
        if n % i == 0:
            divs.append(i)
    if len(divs) > 1:
        return False
    else:
        return True
    
def calc_primo_full(n):
    if n < 2:
        return False
    if n == 2: #Dois é o único primo par!
        return True
    if n % 2 == 0: #Tirar de cara os números pares.
        return False
    for i in range(3,int(n**1/2) + 1,2): #Inicia no 3, caminha até a raiz + 1, e pula de 2 em 2 pulando todos os pares.
        if n % i == 0:
            return False #Note que esse return dentro do for vai fazer com que ele termine no primeiro encontro com um divisor! Não existe desperdício de iterações!
    return True


def teste_primo(lista):
    result = []
    for i in lista:
        if calc_primo(i) == True:
            result.append(i)
    return result

def teste_metade(lista):
    result = []
    for i in lista:
        if calc_primo_metade(i) == True:
            result.append(i)
    return result

def teste_raiz(lista):
    result = []
    for i in lista:
        if calc_primo_raiz(i) == True:
            result.append(i)
    return result

def teste_full(lista):
    result = []
    for i in lista:
        if calc_primo_full(i) == True:
            result.append(i)
    return result

def teste_desempenho(lista):
    teste_primo(lista)
    teste_metade(lista)
    teste_raiz(lista)
    teste_full(lista)

#Repare na diferença de desempenho entre as implementações.
cProfile.run('teste_desempenho(n_ran)')
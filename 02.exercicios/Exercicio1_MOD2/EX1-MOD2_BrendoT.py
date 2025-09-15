# 1 - Utilizando apenas código python, leia o arquivo "nomes.txt" em anexo a este exercício e execute as seguintes tarefas:
# A- Leia o conteúdo e print o resultado na tela.
# B- Verifique o conteúdo de cada linha, como está a formatação? Formate os nomes para que obedeçam ao padrão de escrita, primeira letra de cada nome maiúscula, sem espaços antes ou depois e o que mais for necessário para que tenhamos uma lista de nomes 100% limpos!
# C- Salve o conteúdo limpo num novo arquivo chamado "nomes limpos.txt" com cada nome em uma linha.
"""
with open ("nomes.txt","r",encoding="utf-8") as n:
    dirty_names = n.readlines()
    print (dirty_names)

clean_names = []
for i in dirty_names:
    var = i.split()
    var1 = " ".join(var)
    var2 = var1.title()
    clean_names.append(var2)
clean_names = "\n".join(clean_names)

with open ("nomes limpos.txt","w",encoding="utf-8") as n:
    n.write(clean_names)
"""
# 2- Utilizando apenas código python, leia o arquivo "vendas.csv" e execute as seguintes tarefas:
# A- Leia o conteúdo do arquivo e print o resultado na tela.
# B- Calcule o valor total em vendas.
# C- Printe o valor total em vendas para o usuário.
"""
with open ("vendas.csv","r",encoding="utf-8") as v:
    s_recording = v.readlines()
    print(s_recording)

obj = []
qnt = []
valor = []
for i in s_recording:
    var = i.replace("\n","")
    var1 = var.split(",")
    obj.append(var1.pop(0))
    qnt.append(int(var1.pop(0)))
    valor.append(float(var1.pop(0)))

contador = 0
for i in range(len(obj)):
    contador += qnt[i] * valor[i]

print(f"O valor total de vendas é de R$ {contador:.2f}")   

"""
    
# 3- Construa uma calculadora capaz de realizar as 4 operações matemáticas básicas. Esta calculadora deve obedecer as seguintes regras:
# A- Cada operação matemática deve estar encapsulada em uma função.
# B- Deve existir tratamento de erros/exceções, de forma a prevenir possíveis erros.
# C Deve conter um menu para execução do programa, onde o usuário só saia do programa quando selecionar a opção de sair.

def soma (x,y):
    try:
        return x + y
    except TypeError:
        print("Digite um número válido")
def subtracao (x,y):
    return x - y

def multiplicacao (x,y):
    try:
        return x * y
    except TypeError:
        print("Digite um número válido")
def divisao (x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Não é possível dividir por 0")
    except TypeError:
        print("Digite um número válido")

def user_num ():
    x = float(input("Digite o 1º número"))
    y = float(input("Digite o 2º número"))
    return x,y


controle = True

while controle == True:
    print("Digite 1 para soma")
    print("Digite 2 para subtração")
    print("Digite 3 para multiplicação")
    print("Digite 4 para divisão")
    print("Digite 5 para sair")
    menu = input("Digite a opção desejada:")
    if menu == "1":
        try:
            x,y = user_num()
            print(soma (x,y))
        except ValueError:
            print("Digite um número válido")   
        except TypeError:
            print("Digite um número válido") 
    elif menu == "2":
        try:
            x,y = user_num()
            print(subtracao (x,y))
        except TypeError:
            print("Digite um número válido") 
    elif menu == "3":
        try:
            x,y = user_num()
            print(multiplicacao (x,y))
        except TypeError:
            print("Digite um número válido") 
    elif menu == "4":
        try:
            x,y = user_num()
            print(divisao (x,y))
        except TypeError:
            print("Digite um número válido") 
        except ZeroDivisionError:
            print("Não é possível dividir por 0") 
    elif menu == "5":
        controle = False



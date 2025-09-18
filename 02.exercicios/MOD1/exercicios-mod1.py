# 1- Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.

"""
print("Olá, Mundo!")
"""

# 2- Crie uma variável para armazenar seu nome e em seguida exiba uma mensagem de boas-vindas que inclua seu nome.
"""   
nome = "Brendo"
print("Bem vindo,",nome,"!")
"""
# 3- Crie duas variáveis com números inteiros e exiba a soma delas.
"""
int_1 = 4
int_2 = 5

print(int_1 + int_2)
"""
# 4- Peça ao usuário para digitar seu nome e em seguida exiba uma mensagem de boas-vindas com o nome fornecido.
"""
nome = input("Insira seu nome:")
print("Bem vindo,",nome,"!")
"""

# 5- Peça ao usuário para digitar o ano em que nasceu, calcule e exiba sua idade aproximada.
"""
ano = int(input("Insira o ano de nascimento:"))
idade = 2025 - ano
print("Você tem", idade, "anos!")
"""

# 6- Peça ao usuário para inserir duas notas, calcule a média e exiba o resultado.
"""
nota_1 = float(input("Valor nota 1:"))
nota_2 = float(input("Valor nota 2:"))

print("Sua nota é:",(nota_1 + nota_2)/2," pontos.")
"""

# 7- Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).
"""
idade = int(input("Insira sua idade:"))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
"""

# 8- Peça um número e verifique se ele é positivo, negativo ou zero.
"""
num = float(input("Insira um número:"))
if num == 0:
    print("Seu número é 0!")
elif num > 0:
    print("Seu número é positivo!")
else:
    print("Seu número é negativo!")
"""

# 9- Peça um número e informe se ele é par ou ímpar.
"""
num = int(input("Insira um número:"))
verificacao = num % 2  # verificar se o número é divisivel por 2

if verificacao == 0:
    print("Seu numero é par!")
else:
    print("Seu número é ímpar!")
"""
# 10- Crie uma senha (ex: "1234") e peça para o usuário digitá-la. Informe se a senha está correta ou incorreta.
"""
senha = "1234"

senha_id = input("Insira sua senha:")

if senha == senha_id:
    print("Senha correta!")
else:
    print("Senha incorreta!")
"""
# 11- Peça o valor de uma compra e, se for maior que R$ 100,00, aplique um desconto de 10%. Exiba o valor final.
"""
valor = float(input("Insira o valor da compra:"))

if valor > 100.0:
    print ("O valor da compra com 10% de desconto é:\n","R$",valor - (valor * 0.1))
else:
    print ("O valor da sua compra permanece R$", valor)
"""
# 12- Peça uma letra ao usuário e verifique se é uma vogal ou uma consoante.
"""
vogais = ["a","e","i","o","u"]

user_vogal = input("Adicione uma letra:")

if user_vogal in vogais:
    print("Sua letra é uma vogal.")
else:
    print("Sua letra é uma consoante.")
"""
# 13- Peça dois números e informe qual deles é o maior, ou se são iguais.
"""
user_n1 = float(input("Insira o primeiro número:"))
user_n2 = float(input("Insira o segundo número:"))

if user_n1 > user_n2:
    print("O número",user_n1, "é maior que o número", user_n2)
elif user_n1 < user_n2:
    print("O número",user_n2, "é maior que o número", user_n1)
else:
    print("Os números são iguais!")
"""
# 14- Crie um programa que exiba os números de 1 a 10.
"""
for i in range (11):
    print(i)
"""
# 15- Peça um número ao usuário e exiba a tabuada de multiplicação desse número, de 1 a 10.
"""
user_num = int(input("Insira um número:"))
for i in range (1,11):
    print (i * user_num)
"""
# 16- Peça números ao usuário até que ele digite 0. Ao final, exiba a soma de todos os números digitados.
"""
x = 1
lista_num = []

while x != 0:
    user_n = float(input("Insira um número:"))
    lista_num.append(user_n)
    x = user_n

contador = 0
for i in lista_num:
    contador += i 
print(contador)
"""
# 17- Crie um programa que peça uma senha ao usuário. Enquanto a senha não for "1234", continue pedindo.
"""
user_senha = int(input("Insira sua senha:"))

while (user_senha != 1234):
   user_senha = int(input("Senha incorreta. Digite novamente!"))
else:
    print("Seja bem vindo(a)!")
"""
# 18- Crie um programa que faça uma contagem regressiva de 10 até 0.
"""
for i in range (11):
    contagem_regressiva = 10
    contagem_regressiva= contagem_regressiva - i
    print (contagem_regressiva)
"""
# 19- Crie um número secreto e peça ao usuário para adivinhar. Dê dicas se o palpite foi maior ou menor, até ele acertar.
"""
n_sec = 26
n_user = int(input("Digite um número:"))

while n_user != n_sec:
    n_user = int(input("Digite outro número:"))
    if n_user > n_sec:
        print("O número secreto é menor que o número digitado!")
    elif n_user < n_sec:
        print("O número secreto é maior que o número digitado!")
print("Você acertou!")
"""
# 20- Crie um programa que itere de 1 a 20 e exiba apenas os números pares.
"""
for i in range (2,20,2):
    print (i)
"""
# 21- Peça um número e calcule o seu fatorial (ex: 5! = 5 * 4 * 3 * 2 * 1).
"""
nun_fatorial = int(input("Insira um número:"))
multi = 1

for i in range (nun_fatorial):
    contador = nun_fatorial - 1
    contador = nun_fatorial - i #valores para multiplicar
    multi = multi * contador
print (multi)
"""
# 22- Crie uma lista com 5 nomes de frutas e exiba cada fruta da lista.
"""
frutas = ["maça","uva","banana","pêra"]

for i in frutas:
    print (i)
"""
# 23- Crie uma lista vazia e peça ao usuário para inserir 5 itens de uma lista de compras. Ao final, exiba a lista completa.
"""
user_list = []

while len (user_list) != 5:    
        lis_compra = input("Adicione um item na sua lista de compra:")
        user_list.append(lis_compra)

for i in user_list:
        print (i)
"""
# 24- Dada uma lista de notas [7, 8, 5, 9, 6], calcule a média e exiba o resultado.
"""
notas = [7, 8, 5, 9, 6]
contador = 0
for i in notas:
    contador += i 

print(contador/len(notas))
""" 
    
# 25- Dada uma lista de números [10, 23, 4, 7, 15], encontre e exiba o maior e o menor número.
"""vamos 
num = [10, 23, 4, 7, 15]
num.sort()
print("Menor número:",num[0]," Maior número:" ,num[4])
"""
# 26- Crie uma lista de nomes e peça um nome ao usuário. Verifique se o nome está na lista e exiba uma mensagem correspondente.
"""
nomes = ["João","Letícia","Pedro"]
user_name = input("Insira um nome:")
if user_name in nomes:
    print("Seu nome consta na nossa base de dados.")
else:
    print("Seu nome não consta na nossa base de dados.")
"""
# 27- Crie uma função que exiba a mensagem "Bem-vindo ao programa!" e em seguida chame essa função.
"""
def bem_vindo ():
    return print("Bem-vindo ao programa!")
bem_vindo()
"""
# 28- Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.
"""
nome = input("Insira o seu nome:")

def saudacao (n1):
    return print ("Seja bem vindo(a),", n1,"!")

saudacao (nome)
"""
# 29- Crie uma função que receba dois números como parâmetros e retorne a soma deles.
"""
n1 = float(input ("Insira um número"))
n2 = float(input ("Insira um número"))

def soma (num1, num2):
    return num1 + num2

print (soma(n1,n2))
"""
# 30- Crie uma função que receba uma lista de números como parâmetro e retorne a média dos valores.
"""
notas = [7, 8, 5, 9, 6]
def media (lista):
    contador = 0
    for i in lista:
        contador += i 
    return(contador/len(lista))
print(media(notas))
"""
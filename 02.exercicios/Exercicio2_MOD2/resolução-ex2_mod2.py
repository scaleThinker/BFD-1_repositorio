# 1 - Crie uma função chamada "gera_lista".
# Essa função deve receber como parâmetro um número inteiro com o total de números que a lista deve conter, e retornar a lista gerada.
# Os números devem ser do tipo inteiro e  gerados aleatoriamente utilizando a biblioteca random.
# Exemplo de chamada: gera_lista(5)
# Exemplo de retorno: [6,25,60,16,5]
"""
import random
def geralista(n:int):
    var=[]
    for i in range(n):
        var.append(random.randint(0,1000))
    return var
"""
# 2 - Crie uma função chamada "analisar_numeros". 
# Essa função deve receber como parâmetro uma lista contendo 200 números gerados a partir da função do exercício 1 e 
# retornar um dicionário contendo as seguintes informações:
# A - O total de números na lista
# B - A quantidade de números pares
# C - A quantidade de números ímpares
# D - A soma de todos os números
# E - A média dos números
# F - Os números primos presentes na lista.
"""
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
"""
# 3 - Utilizando o arquivo "contatos.txt", crie uma função chamada "limpa_tel" 
# deve receber dois parâmetros, arquivo_entrada e arquivo_saida. 
# A função deverá limpar os dados contidos no arquivo e produzir um novo arquivo contendo somente os números de telefone, 
# sem espaços ou caracteres especiais, 1 telefone por linha, com o nome escolhido através do parâmetro "arquivo saída".
"""

def limpa_tel (arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "r", encoding="utf8") as cont:
        contatos = cont.readlines()
   
    clean=[]
    
    for i in contatos:
        digitos = ''.join(filter(str.isdigit, i))
        clean.append(digitos)
    
    lista = ""

    for i in clean:
        lista += i +"\n"
        print(lista)

    with open (arquivo_saida, "w", encoding="utf8") as limpo:
        limpo.write(lista)

limpa_tel("contatos.txt","limpo.txt")
"""
# 4 - Crie uma classe chamada "Filme". Siga as instruções na sequência:
# A - Os atributos de instância a serem inicializados devem ser: titulo, diretor, ano_lancamento, duracao, nota_imdb. 
# B - A classe deve conter um método chamado detalhes, 
# que retorna uma string contendo o titulo do filme, o nome do diretor, o ano em que foi lançado, sua duracao e sua nota no imdb.
# C - Crie pelo menos 3 instâncias para demonstrar o uso.

"""
class Filme:
    def __init__(self,titulo,diretor,ano_lancamento,duracao,nota_imdb):
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento
        self.duracao = duracao
        self.nota_imdb = nota_imdb
    
    def detalhes(self):
        return f"O filme '{self.titulo}' foi dirigido por {self.diretor} em {self.ano_lancamento} com {self.duracao} de duração. Recebeu {self.nota_imdb} no imdb"

filme1=Filme("A Viagem de Chihiro","Hayao Miyazaki",2003,"2h5m",8.6)
filme2=Filme("O Homem Invisível","Leigh Whannell",2020,"2h4m",7.1)
filme3=Filme("Pokémon: O Filme - Mewtwo contra-ataca","Kunihiko Yuyama",1998,"1h36m",6.3)

print(filme1.detalhes())
print(filme2.detalhes())
print(filme3.detalhes())
"""
# 5 - Crie uma classe chamada "Termometro". Siga as instruções na sequência.
# A - O atributo de inicialização deve ser: temperatura_celsius.
# B - Crie dois métodos: "aumentar_temp(valor)" e "diminuir_temp(valor)". Os métodos devem ser capazes de alterar a temperatura segundo o valor imputado.
# C - Crie um terceiro método: "temperatura_atual" que deve printar na tela a temperatura naquele momento.
# D - Crie um quarto método: "converte_farenheit" que deve calcular e retornar a temperatura atual convertida para farenheit.
# Para teste utilize os seguintes valores:
# Inicia em 25
# Exibe temperatura
# Aumenta em 25
# Exibe temperatura
# Diminui em 50
# Exibe temperatura
# Converte para Farenheit e exibe na tela.

"""
class Termometro:
    def __init__(self,temperatura_celsius:float):
        self.temperatura_celsius = temperatura_celsius

    def aumentar_temp(self):
        try:
            temp = float(input("Insira a temperatura a ser acrescida:"))
            self.temperatura_celsius += temp
            return self.temperatura_celsius  
        except ValueError:
            print("Digite um valor válido!")
    def diminuir_temp(self):
        try:
            temp = float(input("Insira a temperatura a ser subtraída:"))
            self.temperatura_celsius -= temp
            return self.temperatura_celsius
        except ValueError:
            print("Digite um valor válido!")
    def temperatura_atual(self):
        return f"A temperatura atual é {self.temperatura_celsius:.2f} °C."
    def  converte_farenheit (self):
            return f" A temperatura em fahrenheit é: {self.temperatura_celsius * (9/5) + 32} °F"


temp = Termometro(25)

print(temp.temperatura_atual())
print(temp.aumentar_temp())
print(temp.temperatura_atual())
print(temp.diminuir_temp())
print(temp.temperatura_atual())
print(temp.converte_farenheit())
"""
"""
É importante notar que a estrutura "class" funciona para múltiplas finalidades.

Na maioria dos casos, nós utilizaremos o método __init__ como primeiro método de uma classe
para garantir que o objeto seja inicializado seguindo as regras de criação e seus atributos.

O objetivo é garantir que cada instância criada a partir daquela classe, tenha o estado inicial
como definido pela classe.
"""

#Exemplo já utilizado anteriormente:

class Pessoa: 
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano

#Ao inicializarmos um objeto da classe Pessoa, precisamos seguir suas regras de inicialização!
#Do contrário obteremos um erro, repare:

p1 = Pessoa("Caio","caio@meubigemail.com","ULTRAMEGAPREMIUM") #Código funcional
# p2 = Pessoa("Arg1","Arg2 sem arg3") #Código que dará erro, acusa a falta de um argumento.

#Vamos a um segundo exemplo:

class Cliente():
    nome = "Caio"
    email = "caio@meubigemail.com"

c1 = Cliente()

print(c1.nome)

#Repare que a saída do código acima é um atributo fixo declarado na classe Cliente
#O que é completamente possível, sem inicializador!
#No entanto, sem o __init__, não podemos inicializar uma instância diferente da classe
#sempre que eu quiser e seguindo sempre as mesmas regras, e cada uma com dados próprios.

"""
Então nunca utilizaremos o class sem o def __init__()?
Não! Existem alguns cenários como o do exemplo do polimorfismo em que isso pode ocorrer.
São dois exemplos:
1 - Agrupadores lógicos de métodos (estáticos).
2 - Contêineres de constantes e configurações.

Vamos entender com exemplos esses dois casos:

"""

# 1 - Agrupadores de métodos:

class FormatadorDeDados:
    """
    Agrupa vários métodos para transformação de dados. Não necessita inicializador
    pois não há estado para gerenciar, nem individualidade necessária para cada objeto.
    Só é necessário descrever e utilizar funcionalidades a partir dela.
    """

    def txt_para_csv(dados):
        print("Lógica para converter de txt para csv")

    def csv_para_txt(dados):
        print("Lógica para converter de csv para txt")

#Exemplo de uso:

arquivo = "Aqui contém dados"

FormatadorDeDados.csv_para_txt(arquivo)
FormatadorDeDados.txt_para_csv(arquivo)

#Repare que não inicializamos nenhum objeto apartir da classe
#Nós só chamamos os métodos para utilizar suas funcionalidades diretamente
#Nessa perspectiva, a classe apenas agrega uma série de métodos e funcionalidades.

#2 - Contêineres de constantes e configurações:

class ConfiguracoesProjeto():
    """
    Esta classe irá conter apenas variáveis que contém configurações para serem acessadas
    no momento oportuno, mantendo tudo no mesmo lugar!
    """
    NOME_DO_PROJETO = "Python Back-End BFD"
    VERSAO = "2.3.0"
    IP = "192.168.0.1"
    PORT = 8080
    PROTOCOL = "HTTPS"
    TIMOUT_DEFAULT = 15 #segundos

#Exemplo de uso:

#Imagine que aqui estamos numa função que precisamos dizer
#Qual ip e qual porta um cliente deve se conectar:

def connect(IP,PORT):
    "Executa uma lógica de conexão utilizando um ip e uma porta"
    print(f"Conectando-se ao ip {IP} na porta {PORT}")

connect(ConfiguracoesProjeto.IP,ConfiguracoesProjeto.PORT)

#Através dessa centralização podemos facilmente criar grandes arquivos de configuração
#Centralizados e organizados.
#Para qualquer config que você precise, basta importar o módulo que detém as configurações
#E utilizá-las a partir da chamada no formato: nome_da_classe.nome_da_config
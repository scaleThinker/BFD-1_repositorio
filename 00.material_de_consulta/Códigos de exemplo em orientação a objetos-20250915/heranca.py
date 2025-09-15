#Para trabalharmos o conceito de herança, vamos utilizar o mesmo exemplo que os anteriores.
class Pessoa: 
    total_pessoas = 0
   
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano

        Pessoa.total_pessoas += 1

    def verificar_plano(self):
        return f"A pessoa {self.nome} está no plano '{self.plano}'."
    
#Vamos criar uma classe filha para que ela herde nossa classe mãe!
class Vip(Pessoa):
    
    def __init__(self, nome, email,servico):
        #Na sequência faremos dois processos:
        #chamar a função super() para inicializar o construtor da classe mãe, reaproveitando código!
        super().__init__(nome,email,plano="Vip") #Nosso plano aqui é sempre vip por design!

        #Definir atributos que diferem a classe filha, da mãe:
        self.servico = servico

    #Podemos declarar métodos com os mesmos nomes dos da classe mãe
    #mas modificar seu comportamento, um exemplo de polimorfismo.

    def verificar_plano(self):
        return f"Nosso VIP {self.nome} está no plano {self.plano}"
    
    #E também declarar métodos específicos da classe filha:
    
    def verifica_servico(self):
        return f"O servico escolhido pelo VIP {self.nome} foi {self.servico}"
    

#Até esta etapa, fizemos apenas declarações, vamos criar objetos e ver como funciona a herança

pessoa_free = Pessoa(nome="Caio", email = "caio@email.com", plano="free")
pessoa_vip = Vip(nome="Antônio",email="antonio@email.com",servico = "Frete Grátis")

#Com os objetos declarados, vamos verificar os pontos chave:

print(pessoa_free.verificar_plano())

print(pessoa_vip.verificar_plano())

#Repare na diferença entre as saídas existentes, mesmo chamando a função de mesmo nome!
#O fato dos métodos terem o mesmo nome, não indica que tem a mesma origem!!!

#Vamos olhar o servico especial escolhido pelo VIP:

print(pessoa_vip.verifica_servico())

#Retire o comentário da linha a seguir e tente executá-lo: O que acontece? Porque acontece?

# print(pessoa_free.verifica_servico())


#Agora comente novamente o código acima
#E tente comentar o método verifica_plano() da classe filha e executar novamente o código
#O que acontece? Porque acontece?

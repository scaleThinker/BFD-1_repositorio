class Pessoa: #Lembrando da boa prática da inicial das classes em maiúscula!
    """
    Representa uma pessoa em nosso sistema.
    Cada pessoa criada a partir desta classe será um objeto separado.
    Como dito em aula, ela é nossa definição!
    """
    
    #A primeira função é sempre o __init__(self,atributos)
    #Ela também é conhecida como construtor: é chamado quando um novo objeto Pessoa é criado.
    #'self' representa a instância específica que está sendo criada.
    def __init__(self, nome, email, plano):
        # Atributos de Instância: dados que pertencem a cada objeto individualmente.
        self.nome = nome
        self.email = email
        self.plano = plano

    #Método de Instância: uma função que pertence ao objeto.
    #Ele pode acessar e modificar os atributos da instância usando 'self'.
    def verificar_plano(self):
        return f"A pessoa {self.nome} está no plano '{self.plano}'."

#Instanciação:
#Vamos criar dois objetos diferentes a partir da mesma classe.
Pessoa1 = Pessoa(nome="Maria", email="maria@email.com", plano="Free")
Pessoa2 = Pessoa(nome="João", email="joao@email.com", plano="Premium")

#Acessando atributos dos objetos
#Repare na sintaxe: objeto.atributo
print(f"Nome da Pessoa 1: {Pessoa1.nome}")

#Chamando métodos dos objetos
#Repare na sintaxe: objeto.método
print(Pessoa2.verificar_plano())
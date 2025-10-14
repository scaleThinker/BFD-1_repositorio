class Pessoa: #Lembrando da boa prática da inicial das classes em maiúscula!
    #Nós podemos diferenciar atributos da classe para os atributos de instâncias
    #Se um atributo for definido na classe, ele pertence a classe!
    total_pessoas = 0
    #Para definir um atributo de instância basta declará-lo na __init__ como já fizemos:
    
    def __init__(self, nome, email, plano):
        # Atributos de Instância: dados que pertencem a cada objeto individualmente.
        self.nome = nome
        self.email = email
        self.plano = plano

        #Vamos adicionar um na variável da classe a cada criação de uma nova instância:
        Pessoa.total_pessoas += 1

    def verificar_plano(self):
        return f"A pessoa {self.nome} está no plano '{self.plano}'."

#Podemos verificar a quantidade de pessoas, antes da criação das instâncias:
print(f"Total de pessoas antes da criação de instâncias: {Pessoa.total_pessoas}")

Pessoa1 = Pessoa(nome="Maria", email="maria@email.com", plano="Free")
Pessoa2 = Pessoa(nome="João", email="joao@email.com", plano="Premium")

#E depois da criação das instâncias:
print(f"Total de pessoas depois das instâncias: {Pessoa.total_pessoas}")

#Repare que nesse caso, o atributo de uma classe, por ser parte de sua definição
#poderá ser acessado também por meio das instâncias(objetos) criadas.

print(f"Total de pessoas visualizado através do objeto Pessoa1: {Pessoa1.total_pessoas}")
print(f"Total de pessoas visualizado através do objeto Pessoa2: {Pessoa2.total_pessoas}")

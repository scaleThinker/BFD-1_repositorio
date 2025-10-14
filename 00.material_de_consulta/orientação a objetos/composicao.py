"""
A composição é uma forma mais forte da relação "Tem-um". 
Aqui, a "parte" não faz sentido e não pode existir sem o "todo".

"""

class Motor:
    def __init__(self, potencia, tipo="Combustão"):
        self.potencia = potencia
        self.tipo = tipo

    def ligar(self):
        print(f"Motor de {self.potencia}cv ligado!")


class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        #O objeto Motor é CRIADO AQUI DENTRO. Ele pertence ao Carro.
        self.motor = Motor(potencia_motor)

    #O Carro delega a ação de "ligar" para seu componente Motor
    def ligar_carro(self):
        print(f"Ligando o {self.modelo}...")
        self.motor.ligar() #repare como este método chama o método de um objeto instanciado.

#Quando criamos um carro, o Motor é criado automaticamente junto
meu_fusca = Carro("Fusca", 50)

#Não acessamos o motor diretamente. A interação é feita através do Carro.
meu_fusca.ligar_carro()

#O objeto "motor" do Fusca só existe enquanto o "meu_fusca" existir.
#Sem o "meu_fusca", não faz sentido instanciar um objeto de "motor" isoladamente.


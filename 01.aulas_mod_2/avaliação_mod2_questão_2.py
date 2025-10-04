# 2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
# A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.
# B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.
# C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes 
# e alterar informações dos clientes. Não deve ser possível ter saldo negativo, nem sacar além do saldo.
# Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def consultar_dados(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}'
    
    def alterar_dados(self, nome=False, cpf=False, endereco=False):
            if nome is not False:
                self.nome = nome
            if cpf is not False:
                self.cpf = cpf
            if endereco is not False:
                self.endereco = endereco
            return "Dados atualizados com sucesso!"

class Conta_corrente(Cliente):
    def __init__(self, nome, cpf, endereco, saldo=0.0):
        super().__init__(nome, cpf, endereco)
        self.__saldo = saldo
    
    def consultar_saldo(self):
        return f"Saldo atual: R$ {self.__saldo:.2f}"        
    
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        return "Valor inválido para depósito!"
    
    def sacar(self, valor: float):
        if valor > self.__saldo:
            return f"Saldo insuficiente! Saldo atual: R$ {self.__saldo:.2f}"
        if valor <= 0:
            return "Valor inválido para saque!"
        self.__saldo -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso!"
    
    def consultar_dados(self):
        dados_basicos = super().consultar_dados()
        return f"{dados_basicos}\nSaldo: R$ {self.__saldo:.2f}"

conta = Conta_corrente("Brendo Tavares", "123.456.789-00", "Praia Vermelha, 123")


print(conta.consultar_dados())
print(conta.consultar_saldo())
print(conta.depositar(1000))
print(conta.consultar_saldo())
print(conta.sacar(300))
print(conta.consultar_saldo())
print(conta.sacar(800))
print(conta.consultar_saldo())

print(conta.alterar_dados(nome="Brendo Tavares dos Santos", endereco="Gragoatá, 456"))
print(conta.consultar_dados())

print(conta.sacar(-50))
print(conta.consultar_saldo())

print(conta.depositar(-100))
print(conta.consultar_saldo())
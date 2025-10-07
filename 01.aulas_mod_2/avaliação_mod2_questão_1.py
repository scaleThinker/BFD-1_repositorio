# 1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:
# A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.
# B - Crie um método para retornar cada atributo.
# Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.

class Carro:
    def __init__(self, modelo, marca, ano_lancamento, potencia, tp_cambio, valor_lancamento):
        self.modelo = modelo
        self.marca = marca
        self.ano_lancamento = ano_lancamento
        self.potencia = potencia
        self.tp_cambio = tp_cambio
        self.valor_lancamento = valor_lancamento
    
    #Criei as funções para retornar os atributos, por mais que consiga acessar direto no objeto.
    def get_modelo(self):
        return self.modelo
    
    def get_marca(self):
        return self.marca
    
    def get_ano_lancamento(self):
        return self.ano_lancamento
    
    def get_potencia(self):
        return self.potencia
    
    def get_tp_cambio(self):
        return self.tp_cambio
    
    def get_valor_lancamento(self):
        return self.valor_lancamento
    
    #Retorna as infos em f-string por que não se objetiva trabalhar com esse retorno depois. 
    def info_completa(self):
        return f"O carro {self.modelo} é da marca {self.marca}, com potencia {self.potencia}, possui câmbio {self.tp_cambio}. Foi lançado em {self.ano_lancamento} no valor valor de R$ {self.valor_lancamento:.2f}."

carro1 = Carro("Onix", "Chevrolet", 2020, "1.0", "manual", 60000.00)
carro2 = Carro("HB20", "Hyundai", 2019, "1.6", "automático", 70000.00)
carro3 = Carro("Polo", "Volkswagen", 2021, "1.0", "automático", 75000.00)

print("~~~~~ Carro 1 ~~~~~")
print(carro1.get_modelo())
print(carro1.get_marca())
print(carro1.get_ano_lancamento())
print(carro1.get_potencia())
print(carro1.get_tp_cambio())
print(carro1.get_valor_lancamento())
print(carro1.info_completa())

print("~~~~~ Carro 2 ~~~~~")
print(carro2.get_modelo())
print(carro2.get_marca())
print(carro2.get_ano_lancamento())
print(carro2.get_potencia())
print(carro2.get_tp_cambio())
print(carro2.get_valor_lancamento())
print(carro2.info_completa())

print("~~~~~ Carro 3 ~~~~~")
print(carro3.get_modelo())
print(carro3.get_marca())
print(carro3.get_ano_lancamento())
print(carro3.get_potencia())
print(carro3.get_tp_cambio())
print(carro3.get_valor_lancamento())
print(carro3.info_completa())
"""
class Aluno: #primeira letra maiuscula

    def __init__(self,name,sexo,idade,nota1b,nota2b): #a primeira def sempre __init__
        self.name=name #o self é um atributo que referencia ele mesmo
        self.sexo=sexo
        self.idade=idade
        self.nota1b=nota1b
        self.nota2b=nota2b

    def verificaridade(self):
        return f"A idade do(a) aluno(a) é {self.idade} anos."
    
    def medianotas(self):
        mediab=(self.nota1b + self.nota2b)/2
        return f"A média do(a) aluno(a) {self.name} é {mediab} pontos."
    
aluno1=Aluno(name="João da Silva",sexo = "M", idade=14, nota1b=4.5, nota2b=7.8)
aluno2=Aluno(name="Maria Joaquina da Motta",sexo="F", idade=13, nota1b=8.2, nota2b=6.8)

print(f"O nome do(a) aluno(a) é {aluno1.name}")

print(aluno2.medianotas())
"""

class Car:
    def __init__(self, year, status, avgas):
        self.year=year
        self.status=status
        self.avgas= avgas 

    def ver_status(self):
        if self.status == True:
            return f"O carro está ligado."
        else:
            return f"O carro está desligado."
    
    def ver_agas(self):
        if self.avgas >= 0.9:
            return f"Gasolina em status seguro."
        elif self.avgas < 0.9 and self.avgas > 0.5:
            return f"Abasteça em breve."
        elif self.avgas < 0.5:
            return f"Abasteça!"
    
    def ver_ipva(self):
        if self.year >= 2015:
            return f"O carro deve pagar IPVA."
        elif self.year < 2015:
            return f"O carro não precisa pagar IPVA."
    
    def rest_ipva(self):
        if self.year < 2015:
            return f"O carro não precisa pagar IPVA."
        elif self.year > 2015:
            t_rest_ipva = 10 - (2025 - self.year)
            return f"Seu carro irá parar de pagar IPVA em {t_rest_ipva} anos."
    def car_off (self):
        status = self.status = False
        return status
        

car1 = Car (year = 1990, status = True, avgas = .30)
car2 = Car (year = 2019, status = False, avgas = .77)
car3 = Car (year = 2024, status = True, avgas = .51)

print(car1.ver_agas())
print(car3.car_off())
print(car2.ver_ipva())
print(car1.ver_status())
print(car2.rest_ipva())
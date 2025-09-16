"""
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
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
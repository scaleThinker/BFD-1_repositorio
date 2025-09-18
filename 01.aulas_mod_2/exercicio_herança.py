#Produza uma classe Pessoa com 3 atributos.
#Produza 2 classes, Aluno e Professor.
#Elas devem ser filhas de Pessoa.
#Cada uma deve ter no mínimo 2 atributos adicionais e 3 métodos cada.

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome=nome
        self.idade=idade
        self.email=email

    def mudar_email(self):
        self.email = input("Insira novo email.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, serie, matricula,status="Matriculado"):
        super().__init__(nome,idade,email)
        self.serie=serie
        self.matricula=matricula
        self.status=status

    def desmatricula(self):
        self.status="Cancelado"
    
    def alterar_matricula(self):
        self.matricula=int(input("Insira a nova matrícula"))
    
    def resumo_cadastro(self):
        return f"O(A) aluno(a) {self.nome}, possui {self.idade} anos, está {self.status} sob matrícula Nº {self.matricula} no {self.serie} ano. Email cadastrado: {self.email}"
        

class Professor(Pessoa):
    def __init__(self, nome, idade, email, salario:float, disciplina, turno):
        super().__init__(nome,idade,email)
        self.salario=salario
        self.disciplina=disciplina
        self.turno=turno
    
    def aumentar_sal(self):
        incremento=int(input("Insira o incremento do salário em %"))/100
        self.salario=(self.salario*incremento)+self.salario
    
    def resumo_cadastro(self):
        return f"O(A) professor(a) {self.nome}, possui {self.idade} anos, está lecionando a disciplina {self.disciplina} no turno da {self.turno}, recebendo R$ {self.salario} mensais. Email cadastrado: {self.email}"

    def aprovar(self):
        print(f"Professor aprova aluno.")
    def reprovar(self):
        print(f"Professor reprova aluno.")

aluno1=Aluno(nome="Cleiciane Marlenne Josilda",idade=14,email="cleiciane@edu.br",serie="3º",matricula=121026027)
professor1=Professor(nome="Lucio Costa Abreu Clementino",idade=58,email="costalucio@edu.br",salario=4.898,disciplina="História",turno="Manhã") 

print(aluno1.resumo_cadastro())
print(professor1.resumo_cadastro())
aluno1.desmatricula()
professor1.aprovar()
professor1.aumentar_sal()
print(professor1.resumo_cadastro())



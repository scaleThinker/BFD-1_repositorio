"""Crie um banco de dados
Cria uma tabela com as seguintes colunas:
- ID
- Nome
- Idade
- CPF
- Email
- Endereço
- Sexo
- Salario"""
import sqlite3

con = sqlite3.connect("exemplo_2")
cursor = con.cursor()

print("Banco de dados conectado com sucesso!")

cursor.execute(""" CREATE TABLE IF NOT EXISTS cadastro (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               cpf TEXT NOT NULL,
               email TEXT NOT NULL,
               endereço TEXT NOT NULL,
               sexo TEXT NOT NULL,
               salario INTEGER); """)

print("Tabela criada com sucesso!")

con.commit()

def inserir (tabela,nome,idade,cpf,email,endereço,sexo,salario):
     cursor.execute(f"INSERT INTO {tabela} (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?,?,?,?,?,?,?)", 
                    (nome,idade,cpf,email,endereço,sexo,salario))

con.commit()
# print("Dados inseridos com sucesso!")

# inserir("cadastro","Lorena Maria Silva",24,"12345678912","lorena.maria@gmail.com","Rua das Flores, 10","F",1452.50)
# inserir("cadastro","Marlon Barreto",51,"98765432125","marlon.barr@gmail.com","Avenida Central, 125","M",14332.88)
# inserir("cadastro","Maria Bethania Tavares Nunes dos Santos",32,"14725836998","bethania.maria@gmail.com","Flor de Liz, 225","F",9500.66)

# con.commit()

cursor.execute("SELECT * FROM cadastro")
resultado = cursor.fetchall()

print("Dados de clientes")

print("=="*30)
for i in resultado:
    print(f"ID: {i[0]}, Cliente: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, Email: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}")
print("=="*30)

con.close()
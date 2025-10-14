#Parece inserir dados no nosso banco o processo de conexão será semelhante ao executado anteriormente.

import sqlite3

con = sqlite3.connect("exemplo.db")

cursor = con.cursor()

#Com nossa conexão e cursor prontos, podemos inserir dados na nossa tabela.
#Existem vários comandos para essa tarefa, vamos ver apenas 1 por enquanto.

cursor.execute("INSERT INTO cliente (nome, email) VALUES (?, ?)",
               ("Caio","caio@email.com"))

cursor.execute("INSERT INTO cliente (nome,email) VALUES (?,?)",
               ("Vin Diesel","dieselvin@email.com"))

#Notem que no momento de inserir dados precisamos obedecer o formato no qual a tabela que irá receber os dados foi criada.
#Repare também que no outro arquivo criamos um tabela que contém ID, mas aqui não precisamos inserir dados para ele
#Isso porque ele foi configurado como auto-incremento, significando que ele será inserido automaticamente pelo banco.

#Agora precisamos fazer nosso commit!

con.commit()

print("Dados inseridos com sucesso!")

con.close()
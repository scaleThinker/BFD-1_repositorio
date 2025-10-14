import sqlite3


con = sqlite3.connect("exemplo.db")
cursor = con.cursor()

#Agora vamos consultar os dados que inserimos na nossa tabela cliente.

cursor.execute("SELECT * FROM cliente;")

#Após a execução desse comando, precisamos de uma variável para guardar os resultados trazidos pela query.

resultado = cursor.fetchall() #Esse método recupera todos os resultados que a consulta feita no execute trouxer!

#Como teremos vários resultados sendo recuperados, preparamos uma estrutura para printar na tela.

print("Lista de clientes")

print("=="*30)
for i in resultado:
    print(f"ID: {i[0]}, Cliente: {i[1]}, Email: {i[2]}")

print("=="*30)
print("\n")

#Podemos fazer uma consulta com filtros também:

cursor.execute("SELECT * FROM cliente WHERE email = 'dieselvin@email.com';") #Apenas emails que sejam iguais a dieselvin@email.com
email = cursor.fetchall()

print("Emails do vin diesel:\n")

for e in email:
    print(f"ID {e[0]}, Nome: {e[1]}, Email: {e[2]}")

con.close()

#bigquerry para achar base de dados
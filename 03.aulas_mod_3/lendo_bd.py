import sqlite3

con = sqlite3.connect("exemplo_2")
cursor = con.cursor()

cursor.execute("SELECT * FROM cadastro;")
resultado = cursor.fetchall()

print("=="*30)
for i in resultado:
    print(f"ID: {i[0]}, Cliente: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, Email: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}")
print("=="*30)

con.close()
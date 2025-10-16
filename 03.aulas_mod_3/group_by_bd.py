import sqlite3

con = sqlite3.connect("exemplo_2")
cursor = con.cursor()


cursor.execute("""SELECT nome, salario, MIN(idade) AS maduros
                FROM cadastro
                WHERE idade > 30 
                GROUP BY nome, salario;""")

con.commit()

resultado = cursor.fetchall()

print("=="*30)
for i in resultado:
    print(f"Cliente: {i[0]}, Salário: {i[1]}")
print("=="*30)

con.close()
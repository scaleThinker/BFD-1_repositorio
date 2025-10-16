import sqlite3

con = sqlite3.connect("exemplo_2")
cursor = con.cursor()

cursor.execute("""SELECT nome, salario 
               FROM cadastro
               ORDER BY salario ASC;""")

con.commit()

resultado = cursor.fetchall()

print("=="*30)
for i in resultado:
    print(f"Cliente: {i[0]}, Salário: {i[1]}")
print("=="*30)

con.close()
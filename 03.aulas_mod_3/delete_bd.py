import sqlite3

con = sqlite3.connect("exemplo_2")
cursor = con.cursor()

cursor.execute("DELETE FROM cadastro WHERE ID = 3")

con.commit()

con.close()
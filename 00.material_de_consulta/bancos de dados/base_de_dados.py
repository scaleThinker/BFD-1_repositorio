"""Criando um banco de dados e conectando"""

#Primeiro passo é importar a biblioteca sqlite3
#Repare que não é necessária nenhuma instalação via pip. sqlite3 já vem com a instalação base do Python.
#SGDBs diferentes vão conter algumas pequenas diferenças entre si, bibliotecas diferentes interagem com bancos diferentes, consulte a documentação do seu SGDB.

import sqlite3

#A sqlite cria um arquivo para servir como banco de dados. Tirando esse detalhe a conexão com bancos de dados via python não vai variar muito entre bancos.

#Instanciamos um objeto de conexão para conectar com o banco.
con = sqlite3.connect("exemplo.db") #Se o arquivo ainda não existir, ele será criado. Note a extensão do arquivo!

#O passo seguinte é criar um cursor. Ele funciona como um ponteiro, um cliente de acesso ao banco que permite executar comandos.

cursor = con.cursor() #Repare como o cursor() é instanciado na variável que criamos para conexão, se con mudar de nome, a instanciação do cursor muda de nome também.

print("Banco de dados conectado com sucesso!")

#Até esta etapa temos nosso banco criado e conectado. Lembre-se sempre de fechar a conexão depois que terminar de usá-la, veremos isso mais abaixo.

#########################################################################################################################################################


"""Criando uma tabela no banco"""

#Precisamos utilizar nosso cursor para executar comandos.
#Os comandos no banco são feitos em SQL (Não se preocupe se o código SQL não parecer muito claro por enquanto).

cursor.execute(""" CREATE TABLE IF NOT EXISTS cliente (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               email TEXTO NOT NULL); """)

#A sintaxe SQL é bem simples, os comandos são normalmente digitados em maiúsculo, e são bem diretos. Nós estudaremos SQL em detalhe!

print("Tabela criada com sucesso!")

#Apenas utilizar o comando execute não é o suficiente para fazer as alterações
#Para salvar as alterações precisamos fazer um commit (isso lembra algo? 😀)

con.commit() #Executa a alteração no banco

con.close() #Fecha a conexão com o banco! Sempre lembre-se de fechar a conexão!


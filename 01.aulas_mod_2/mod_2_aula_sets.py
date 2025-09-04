#SETS, MANIPULAÇÃO DE ARQUIVOS, TRATAMENTO DE DADOS

with open ("arquivo_aula-2.txt","w") as arquivo_aula2:
    #with --> "Com esse arquivo, faça algo." Ele fecha o arquivo ao final do bloco.
    #open --> abre um arquivo (nome do arquivo, o que fazer com o arquivo)
    #as --> apelidar coisas. Interprete o arquivo como ...
    arquivo_aula2.write(
        """Testando a função .write()
        Adicionando linha 2
        Adicionando linha 3
        Adicionando linha 4
        Adicionando linha 5""")


# with open ("arquivo_aula-2.txt","r") as arquivo_aula2:
#    print(arquivo_aula2.read())"""

# with open ("arquivo_aula-2.txt","r") as arquivo_aula2:
#     print(arquivo_aula2.readline())"""

#with open ("arquivo_aula-2.txt","r") as arquivo_aula2:
#    print(arquivo_aula2.readlines())
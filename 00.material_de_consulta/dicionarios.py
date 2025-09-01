cadastro = {"nome":"João",
            "sobrenome":"da Silva",
            "cpf":"00000000000",
            "endereço":"Rua das flores, n10",
            "sexo":"masculino",
            "conta_corrente":"88888-8"
}

print(cadastro)

#Adicionando um novo par chave-valor (ou atualizar se já existir)
cadastro["devedor"] = False

# print(cadastro)

# #Retornando o valor ligado a uma chave:
# print(cadastro["devedor"])

# #Acessa o valor de uma chave de forma segura. Se a chave não existe, retorna None ou valor padrão.
# print(cadastro.get("sexo"))

# #remove o par chave-valor.
# cadastro.pop("devedor") #Ou del cadastro["devedor"]
# print(cadastro)

# #Retorna todas as chaves:
# print(cadastro.keys())

#Retorna todos os valores:
print(cadastro.values())

# #Retorna todos os pares de chave e valor (útil em loops:)
# print(cadastro.items())

# for i in cadastro.items():
#     print(i)

# for i,j in cadastro.items():
#     print(j)

for i in cadastro.values():
    print(i)
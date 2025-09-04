#MANIPULAÇÃO DE STRINGS

texto = "    Curso Back-EndPython    "

print("#MAIÚSCULAS E MINÚSCULAS")
print ("Lower =\n",texto.lower()) #Converte tudo para minúsculas
print ("Capitalize =\n",texto.capitalize()) #Deixa a primeira letra maiuscula
print ("Upper =\n",texto.upper()) #Converte tudo para maiúscula
print ("Title =\n",texto.title()) #Cada primeira letra maiúscula

print("#LIMPEZA E TRATAMENTO")
print ("Strip =\n",texto.strip("Curso ")) #Remove espaços em branco (no meio não funciona)(ou caractere especificado).
print ("Lstrip =\n",texto.lstrip()) #Remove espaços do início (esquerda)
print ("Rstrip =\n",texto.rstrip()) #Remove espaços do fim (direita)
print ("Replace =\n",texto.replace("Curso","Curso BFD")) #Substitui todas as aparições de uma substring pela nova

print("#BUSCANDO STRINGS E SUBSTRINGS")
print("In =\n","Curso" in texto) #verifica se a substring existe numa string.
print ("Find =\n",texto.find("so")) #retorna o índice da primeira ocorrência da substring procurada.
print ("Index =\n",texto.index("Python")) #igual o .find() mas retorna erro se não encontrar.
print ("Startswith =\n",texto.startswith("Curso")) #Verifica se a string começa com o texto especificado.
print ("Endswith =\n",texto.endswith("Python    ")) #Verifica se a string termina com o texto especificado.

print("#DIVIDIR E JUNTAR")
novotexto = texto.split("-") #Divide uma string em uma lista de substrings a partir do caractere escolhido como separador, se vazio, divide a partir dos espaços.
print ("Split =\n",novotexto)
texto_novo = "".join(novotexto) #oncatena os elementos de uma lista em uma única string (oposto do split). A sintaxe deste método é um pouco diferente do padrão, ele deve ser aplicado ao separador e não a lista.
print ("Join =\n",texto_novo)

print("#VALIDAÇÕES")
print ("Isdigit =\n",texto.isdigit()) #Retorna True se todos os caracteres forem números.
print ("Isalpha =\n",texto.isalpha()) #Retorna True se todos os caracteres são letras do alfabeto.
print ("Isalnum =\n",texto.isalnum()) #Retorna True se todos os caracteres são alfanuméricos (letras ou números).
print ("Isspace =\n",texto.isspace()) #Retorna True se todos os caracteres são espaço em branco ou quebra de linha.

print("#FORMATAÇÃO")
curso = "Python"

dia = "terças e quintas"

num_dec = 0.22556633
print(f"""F-STRING =
O curso de {curso} acontece as {dia}, {num_dec:.2f}""")

print("#ENCODING")

texto = "Olá, fração, decoding"

b_utf = texto.encode('utf-8')

print(b_utf)

texto_decodificado = b_utf.decode('utf-8')

print(texto_decodificado)
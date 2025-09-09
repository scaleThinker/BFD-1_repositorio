#importando bibliotecas
import re
import random
#se nao deu erro na importação, significa que a biblioteca esta instalada.

# estrutura bibliotecas (NOME BIBLIOTECA).(NOME FUNÇÂO)
print(random.randint(1,10)) 

#poderiamos importar apenas uma função de uma biblioteca
from random import randint

randint # agora funciona sem o "random." na frente

# podemos apelidar para facilitar a escrita
import random as r
r.randint(1,40)

# podemos também escolher mais de uma função especifica de uma função
from random import randint, choice

#impoprtando o modulo criado no arquivo mod_2_aula_modulos
import mod2_aula_modulos as m
m.soma

#podemos usar pip no >>> CMD <<< para instalar as bibliotecas.
#ex : pip install pandas

#ALGUMAS BIBLIOTECAS
#django e flask -> frameworks
#requests - requisição para servidores na web
#fastapi - constuir API
#pydantic e pythand-dotenv - palavras passes (variaveis de ambiente)
#pytest - fazer teste
#celery - processamento paralelo (acelerar certas atividades)
#pyJWT - agiliza processos iniciais em web
#SQLAlchemy - trabalhar com sql em python



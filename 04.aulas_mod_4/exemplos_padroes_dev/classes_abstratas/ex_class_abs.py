#Partindo do contexto exposto no documento de conceituação temos o código da primeira implementação:

#Note que abaixo temos duas classes que fazem coisas muito parecidas, mas têm nomes de métodos diferentes
class EmailServico:
    def enviar_email(self, destinatario, assunto, corpo): #Atenção para o nome desse método
        print(f"Enviando email para {destinatario}...")

class SMSServico:
    def mandar_sms(self, numero, texto): #Atenção para o nome deste outro método.
        print(f"Mandando SMS para {numero}...")

#Código para notificar o usuário:
def notificar_usuario(tipo, dados):
    if tipo == 'email':
        servico_email = EmailServico()
        servico_email.enviar_email(dados['email'], "Assunto", "Corpo")
    elif tipo == 'sms':
        servico_sms = SMSServico()
        servico_sms.mandar_sms(dados['numero'], "Texto")
        
# Isso é difícil de manter!
#Nesta estrutura o código principal (que estará em outro arquivo!) precisará saber o nome do método de cada classe
#O que irá criar muita dor de cabeça a medida que a aplicação cresce.
# Vamos refatorar para implementar uma solução!

""" 
    Implementação da solução
"""

#1. Importamos as ferramentas do módulo abc
from abc import ABC, abstractmethod

#2. Criamos o "Contrato" (A Classe Abstrata)
#Note que ela herda de ABC, se você esquecer esse passo não irá funcionar a implementação!
class BaseNotificacao(ABC):
    
    #3. Marcamos o método que **TODAS** as classes filhas DEVERÃO ter
    @abstractmethod #Nosso decorator para implementar o método
    def enviar(self, destinatario, mensagem):
        """Um método obrigatório para enviar uma notificação."""
        #Note que não há código aqui, apenas uma "pass".
        pass

# ******* Agora, forçamos as classes a assinar o contrato *******

#4. EmailNotificacao herda de BaseNotificacao
class EmailNotificacao(BaseNotificacao):
    
    #Ela é OBRIGADA a implementar 'enviar'
    #Note que os parâmetros podem ter nomes diferentes (ex: 'email' em vez de 'destinatario')
    #mas a quantidade de parâmetros deve ser compatível.
    def enviar(self, email, mensagem):
        print(f"LOG: Enviando E-MAIL para {email}: {mensagem}")
        #aqui entra a lógica real de envio
        return True

#5. SMSNotificacao herda de BaseNotificacao
class SMSNotificacao(BaseNotificacao):
    
    # Ela também é OBRIGADA a implementar 'enviar'
    def enviar(self, numero_telefone, mensagem):
        print(f"LOG: Enviando SMS para {numero_telefone}: {mensagem}")
        #aqui entra a lógica real de SMS
        return True

# --- O QUE ACONTECE SE VOCÊ QUEBRAR O CONTRATO? ---

print("--- Tentando quebrar as regras ---")

#REGRA 1: Você não pode instanciar (criar objeto) da classe abstrata
try:
    contrato = BaseNotificacao()
except TypeError as e:
    print(f"ERRO (esperado): {e}")


#REGRA 2: Você não pode "esquecer" de implementar um método abstrato
#Esta regra ajuda muito a manter a arquitetura em vários locais do código.
class NotificacaoIncompleta(BaseNotificacao):
    def __init__(self, tipo):
        self.tipo = tipo
    
    #Oops, esqueci de implementar o método 'enviar'
    def outro_metodo(self):
        print("Fiz outra coisa")

try:
    incompleta = NotificacaoIncompleta("push")
except TypeError as e:
    print(f"ERRO (esperado): {e}")

print("-----------------------------------")


#--- O GRANDE BENEFÍCIO (Polimorfismo) ---

print("\n--- O Benefício (Polimorfismo) ---")

#Agora podemos tratar todos os serviços da MESMA forma
servico_email = EmailNotificacao()
servico_sms = SMSNotificacao()

#Colocamos ambos em uma lista
servicos_de_notificacao = [servico_email, servico_sms]

#O código principal não precisa saber se é Email ou SMS.
#Ele só precisa saber que o objeto "assina o contrato" BaseNotificacao
#e, portanto, COM CERTEZA tem um método .enviar()

for servico in servicos_de_notificacao:
    #O mesmo código funciona para objetos diferentes!
    servico.enviar("123456", "Sua fatura chegou!")

#Polimorfismo significa múltiplas formas

class AutenticadorBDInterno:
    def autenticar(self, credenciais:tuple):
        print(f"Autenticando '{credenciais[0]}' no banco de dados interno...")
        #Lógica: SELECT * FROM usuarios WHERE user = ? AND pass = ?
        return True

class AutenticadorGoogle:
    def autenticar(self, token_google):
        print(f"Autenticando com token do Google...")
        #Lógica: Envia o token para a API do Google para validação
        return True

class AutenticadorFacebook:
    def autenticar(self, token_facebook):
        print(f"Autenticando com token do Facebook...")
        #Lógica: Envia o token para a API do Facebook
        return False #Simulando uma falha

#Função polimórfica: ela funciona com QUALQUER objeto autenticador
#que tenha um método 'autenticar', não importa como ele funciona por dentro.
#E essa é a chave do polimorfismo, essa função confia que o objeto autenticador recebido por ela
#detém um método autenticar

def processar_login(autenticador, credenciais):
    print("--- Tentativa de Login ---")
    if autenticador.autenticar(credenciais): #Aqui é a chave
        print("Login bem-sucedido! Acesso liberado.")
    else:
        print("Falha na autenticação. Acesso negado.")
    print("-" * 25)

#Criando instâncias das diferentes classes de autenticação
auth_bd = AutenticadorBDInterno()
auth_google = AutenticadorGoogle()
auth_facebook = AutenticadorFacebook()

#Chamando a MESMA função 'processar_login' com objetos e credenciais DIFERENTES
processar_login(auth_bd, ("caio.marins", "senhaforte123"))
processar_login(auth_google, "TOKEN_DE_EXEMPLO_GOOGLE")
processar_login(auth_facebook, "TOKEN_DE_EXEMPLO_FACEBOOK")

#Reparem que neste exemplo não utilizamos o __init__ para inicializar um construtor
#em nenhuma das classes, porque isso acontece?

#Olhe o conteúdo da variável inicializada com a classe auth_bd:

print(auth_bd)
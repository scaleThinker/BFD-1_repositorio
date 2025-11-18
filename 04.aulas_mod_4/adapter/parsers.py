#Nossas classes de leitura estão descritas aqui
#Elas implementam as lógicas crus de leitura de cada arquivo
#Deverão ser importadas para a construção do adaptador.

class LeitorDeCSV:
    """Adapter 1: Lê dados de CSV com um método específico."""
    def ler_dados_csv(self, arquivo_path: str) -> str:
        print(f"Adapter CSV: Processando arquivo em '{arquivo_path}'...")
        # Simula a leitura de um arquivo CSV e concatena o texto
        dados = f"DADOS CSV: Cabeçalho, Valor1; Item, Valor2"
        return dados
    

#Note a diferença de nomes dos métodos implementados por cada classe

class LeitorDePDF:
    """Adapter 2: Lê documentos PDF com um método diferente."""
    def obter_conteudo_pdf(self, path: str) -> str:
        print(f"Adapter PDF: Abrindo documento em '{path}'...")
        # Simula a leitura de um PDF
        conteudo = "CONTEÚDO PDF: Relatório Anual de 2023, Página 1 de 5."
        return conteudo
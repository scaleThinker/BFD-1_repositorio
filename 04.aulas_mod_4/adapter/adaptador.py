from parsers import LeitorDeCSV,LeitorDePDF

class LeitorDeDocumentoTarget:
    """Define a interface que o cliente espera para extrair texto."""
    def extrair_texto(self, caminho_arquivo: str) -> str:
        raise NotImplementedError
    #O raise acima é uma forma de podermos implementar um método sem conteúdo
    #Ele será sobrescrito pelo polimorfismo na herança a seguir
    #Ele só define o nome padrão para o método, semelhante ao que acontece métodos abstratos!

    
class LeitorDeArquivosAdapter(LeitorDeDocumentoTarget):
    """
    Adapter que implementa a Target e usa os Adapters por composição.
    Note que essa classe herda o LeitorDeDocumentoTarget e por polimorfismo
    modifica a implementação de extrair_texto dependendo do objeto que será implementado.

    """
    
    def __init__(self, tipo_arquivo: str):
        self._adapter = None #None apenas para poder inicializar.
        tipo = tipo_arquivo.lower()
        
        #O Adapter decide qual Adapter instanciar
        #Note que por ser um if else, só uma das classes abaixo será instanciada!
        
        if tipo == 'csv':
            self._adapter = LeitorDeCSV()
        elif tipo == 'pdf':
            self._adapter = LeitorDePDF()
        else:
            raise ValueError(f"Tipo de arquivo não suportado pelo Adapter: {tipo_arquivo}")

    def extrair_texto(self, caminho_arquivo: str) -> str: #Polimorfismo
        """
        Traduz a chamada Target (CSV ou PDF nesse caso) para o método do Adapter composto.
        """
        if isinstance(self._adapter, LeitorDeCSV):
            #Tradução para o CSV: extrair_texto -> ler_dados_csv
            return self._adapter.ler_dados_csv(caminho_arquivo)
            #Note que no lugar de self._adapter entrará: LeitorDeCSV

        elif isinstance(self._adapter, LeitorDePDF):
            #Tradução para o PDF: extrair_texto -> obter_conteudo_pdf
            return self._adapter.obter_conteudo_pdf(caminho_arquivo)
            #Note que no lugar de self._adapter entrará: LeitorDePDF
        
        else:
            return "Erro: Adaptee não configurado corretamente."
        
#Repare na função isinstance, ela checa se LeitorDeCsv ou LeitorDePDF é um objeto da próxima classe.
#Se for, ele vai chamar o ler_dados_csv(caminho do arquivo) (ou equivalente) 
#que é um método do objeto instanciado (definido nos parsers)
        

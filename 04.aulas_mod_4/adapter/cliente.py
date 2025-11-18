from adaptador import LeitorDeArquivosAdapter, LeitorDeDocumentoTarget

#O cliente usa a mesma função para diferentes tipos de arquivos
def cliente_processa_documento(leitor: LeitorDeDocumentoTarget, nome_arquivo: str):
    print(f"\nCliente: Processando documento '{nome_arquivo}'...")
    texto = leitor.extrair_texto(nome_arquivo)
    print(f"Cliente: Texto extraído:\n>>> {texto}")
    print("---------------------------------")

#Uso
try:
    #1. Adaptador para CSV
    adapter_csv = LeitorDeArquivosAdapter('csv')
    cliente_processa_documento(adapter_csv, "relatorio.csv")

    #2. Adaptador para PDF
    adapter_pdf = LeitorDeArquivosAdapter('pdf')
    cliente_processa_documento(adapter_pdf, "ficha_tecnica.pdf")

except ValueError as e:
    print(f"Erro na criação do Adapter: {e}")
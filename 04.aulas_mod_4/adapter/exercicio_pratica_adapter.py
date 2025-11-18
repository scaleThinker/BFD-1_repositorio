#Numa aplicação o video pode ser mp4 ou avi, mas aplicação so lê mvk

def IdentificadorDeExtensao(arquivo):
    """função para extrair a extensão do arquivo de entrada"""
    extensao_arquivo = arquivo #aqui vai a lógica para buscar a extensão.
    return extensao_arquivo

tipo_arquivo = IdentificadorDeExtensao("Video.avi")

def RecebeArquivo (tipo_arquivo):
    """ Identifica o tipo de arquivo."""
    if tipo_arquivo == "mp4":
        MP4_to_MVK()
    elif tipo_arquivo == "avi":
        AVI_to_MVK()
    else:
        raise ValueError("Tipo não suportado pela aplicação.")

def MP4_to_MVK():
    #lógica para converter de MP4 para MVK
    return

def AVI_to_MVK():
    #lógica para converter de AVI para MVK
    return



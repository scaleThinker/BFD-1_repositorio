import functools

def safe_run(principal):
    """ Decorador para proteger a execução de um serviço contra falhas."""

    @functools.wraps(principal)
    def wrapper(*args, **kwargs):
        try:
            resultado = principal(*args, **kwargs)
            return resultado
        except Exception as e:
            print(f"**ALERTA***: O serviço '{principal.__name__}' falhou com o erro: {e}")
            return None 
    return wrapper

@safe_run
def funcao_quebrada():
    """Uma função quebrada"""
    raise Exception("Ocorreu uma falha inesperada!")

resultado = funcao_quebrada()
import functools

# Define o decorador
def meu_decorador(funcao):
    # Usa functools.wraps para preservar os metadados da função original
    @functools.wraps(funcao)
    # Define a função envelope que envolve a função original
    def envelope(*args, **kwargs):
        # Executa código antes de chamar a função original
        print("faz algo antes de executar")
        # Chama a função original com os argumentos e kwargs
        resultado = funcao(*args, **kwargs)
        # Executa código depois de chamar a função original
        print("faz algo depois de executar")
        # Retorna o resultado da função original
        return resultado
        
    # Retorna a função envelope decorada
    return envelope

# Aplica o decorador à função ola_mundo
@meu_decorador
def ola_mundo(nome, outro_argumento):
    # Corpo da função original
    print(f"Olá mundo {nome}!")
    # Retorna o nome em maiúsculas
    return nome.upper()

# Imprime o nome da função decorada
print(ola_mundo.__name__)


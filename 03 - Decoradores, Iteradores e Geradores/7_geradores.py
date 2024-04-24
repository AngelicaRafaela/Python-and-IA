# Definição da função geradora
def meu_gerador(numeros: list[int]):
    # Loop para iterar sobre cada elemento da lista
    for numero in numeros:
        # A instrução yield produz o próximo valor na sequência do gerador
        # Retorna o número multiplicado por 2 e pausa a execução da função
        yield numero * 2

# Loop for que itera sobre os valores gerados pela função geradora
# Chamada da função meu_gerador com a lista [1, 2, 3]
for i in meu_gerador(numeros=[1, 2, 3]):
    # Imprime cada valor gerado na tela
    print(i)

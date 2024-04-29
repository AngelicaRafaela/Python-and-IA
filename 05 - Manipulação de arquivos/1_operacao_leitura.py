# Abre o arquivo "lorem.txt" no modo de leitura ("r")
arquivo = open("05 - Manipulação de arquivos\lorem.txt", "r")

# Lê o conteúdo completo do arquivo e o imprime
print(arquivo.read())

# Lê a próxima linha do arquivo e a imprime
print(arquivo.readline())

# Lê todas as linhas restantes do arquivo e as imprime como uma lista de strings
print(arquivo.readlines())

# Utiliza um loop while para ler cada linha do arquivo uma por uma
# até que readline() retorne uma string vazia (indicando o final do arquivo)
while len(linha := arquivo.readline()):
    # Imprime cada linha do arquivo
    print(linha)

# Fecha o arquivo após a leitura
arquivo.close()

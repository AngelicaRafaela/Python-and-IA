# Abre o arquivo "teste.txt" no modo de escrita ("w")
arquivo = open("05 - Manipulação de arquivos/teste.txt", "w")

# Escreve uma string no arquivo
arquivo.write("Escrevendo dados em um novo arquivo.")

# Escreve uma lista de strings no arquivo, uma por linha
arquivo.writelines(["\n", "escrevendo", "\n",  "um", "\n",  "novo", "\n", "texto"])

# Fecha o arquivo após a escrita
arquivo.close()

arquivo = open("05 - Manipulação de arquivos\lorem.txt", "r")
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()
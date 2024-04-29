import csv
from pathlib import Path

# Obtendo o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

# Definindo os índices das colunas no arquivo CSV
COLUNA_ID = 0
COLUNA_NOME = 1

try:
    # Tentando criar o arquivo "usuarios.csv" para escrita, com codificação UTF-8
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        # Criando um escritor CSV e escrevendo cabeçalho e linhas de dados
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except ImportError as exc:
    # Se ocorrer um erro de importação, exibir mensagem de erro específica
    print(f"Erro ao criar o arquivo: {exc}")

try:
    # Tentando abrir o arquivo "usuarios.csv" para leitura, com codificação UTF-8
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        # Criando um leitor CSV e iterando sobre as linhas do arquivo
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except ImportError as exc:
    # Se ocorrer um erro de importação, exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo: {exc}")

try:
    # Tentando abrir o arquivo "usuarios.csv" para leitura, com codificação UTF-8, como um dicionário CSV
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as csvfile:
        # Criando um leitor CSV de dicionário e iterando sobre as linhas do arquivo
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    # Se ocorrer um erro de E/S (Input/Output), exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo: {exc}")

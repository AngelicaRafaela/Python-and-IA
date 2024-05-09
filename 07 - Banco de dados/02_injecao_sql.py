import sqlite3  # Importa a biblioteca sqlite3 para trabalhar com o banco de dados SQLite
from pathlib import Path  # Importa a classe Path do módulo pathlib para lidar com caminhos de arquivos

ROOT_PATH = Path(__file__).parent  # Obtém o diretório pai do arquivo atual

# Estabelece uma conexão com o banco de dados SQLite usando o caminho do arquivo 'meu_banco.db'
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Define a função de fábrica de linha para que as linhas retornadas pelo cursor sejam acessíveis por índice e nome da coluna
cursor.row_factory = sqlite3.Row

# Solicita ao usuário que informe o ID do cliente que deseja buscar
id_cliente = input("Informe o id do cliente: ")

# Executa uma consulta SQL para selecionar todos os dados do cliente com o ID fornecido pelo usuário
cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))

# Obtém todos os clientes encontrados pela consulta
clientes = cursor.fetchall()

# Itera sobre os clientes encontrados e imprime seus dados como dicionários
for cliente in clientes:
    print(dict(cliente))  # Converte a linha do banco de dados em um dicionário e imprime

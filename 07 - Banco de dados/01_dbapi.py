import sqlite3  # Importa a biblioteca sqlite3 para trabalhar com o banco de dados SQLite
from pathlib import Path  # Importa a classe Path do módulo pathlib para lidar com caminhos de arquivos

ROOT_PATH = Path(__file__).parent  # Obtém o diretório pai do arquivo atual

# Estabelece uma conexão com o banco de dados SQLite usando o caminho do arquivo 'meu_banco.db'
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

# Cria um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Define a função de fábrica de linha para que as linhas retornadas pelo cursor sejam acessíveis por índice e nome da coluna
cursor.row_factory = sqlite3.Row

# Define funções para interagir com o banco de dados

def criar_tabela(conexao, cursor):
    # Cria uma tabela chamada 'clientes' com colunas 'id', 'name' e 'email'
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), email VARCHAR(150))')
    conexao.commit()  # Confirma a transação no banco de dados

def inserir_registro(conexao, cursor, nome, email):
    # Insere um novo registro na tabela 'clientes' com o nome e email fornecidos
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (name, email) VALUES (?, ?);", data)
    conexao.commit()  # Confirma a transação no banco de dados

def atualizar_registro(conexao, cursor, nome, email, id):
    # Atualiza um registro na tabela 'clientes' com o ID fornecido, definindo o novo nome e email
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET name =?, email =? WHERE id =?;", data)
    conexao.commit()  # Confirma a transação no banco de dados

def exlcuir_registro(conexao, cursor, id):
    # Exclui um registro da tabela 'clientes' com o ID fornecido
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id =?;", data)
    conexao.commit()  # Confirma a transação no banco de dados

def inserir_muitos(conexao, cursor, dados):
    # Insere vários registros na tabela 'clientes' com base nos dados fornecidos
    cursor.executemany("INSERT INTO clientes (name, email) VALUES (?, ?);", dados)
    conexao.commit()  # Confirma a transação no banco de dados

def recuperar_cliente(cursor, id):    
    # Recupera um cliente da tabela 'clientes' com o ID fornecido
    cursor.execute("SELECT * FROM clientes WHERE id =?;", (id,))
    return cursor.fetchone()  # Retorna o primeiro registro encontrado

def listar_cliente(cursor):    
    # Lista todos os clientes da tabela 'clientes' ordenados por nome
    return cursor.execute("SELECT * FROM clientes ORDER BY name;")

# Recupera todos os clientes da tabela 'clientes' e os imprime como dicionários
clientes = listar_cliente(cursor)
for cliente in clientes:
    print(dict(cliente))

# Recupera um cliente específico (ID = 2) da tabela 'clientes' e o imprime como dicionário
cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))

# Imprime os dados do cliente recuperado
print(cliente["id"], cliente["name"], cliente["email"])

# Imprime uma mensagem de boas-vindas com o nome do cliente recuperado
print(f"Seja bem vindo ao sistema {cliente['name']}")

# Exemplo de como inserir múltiplos registros de uma vez
# dados = [
#     ('Angelica', 'angel@gmail.com'),
#     ('Jose', 'jose@gmail.com'),
#     ('Pedro', 'pedro@gmail.com'),
# ]
# inserir_muitos(conexao, cursor, dados)

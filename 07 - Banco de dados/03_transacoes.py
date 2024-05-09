import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (name, email) VALUES (?,?)", ("Teste 3", "teste2@gmail.com"))
    cursor.execute("DELETE FROM clientes WHERE id=6;")
    conexao.commit()    
except Exception as exc:
    print("Ops! Um erro ocorreu! {exc}")
    conexao.rollback()
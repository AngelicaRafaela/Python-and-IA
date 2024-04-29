import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Cria um novo diretório chamado "novo-diretorio" dentro do diretório pai do arquivo em execução
os.mkdir(ROOT_PATH / "novo-diretorio")

# Cria um novo arquivo chamado "novo.txt" e o fecha imediatamente
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomeia o arquivo "novo.txt" para "alterado.txt"
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remove o arquivo "alterado.txt" do sistema de arquivos
os.remove(ROOT_PATH / "alterado.txt")

# Move o arquivo "novo.txt" para dentro do diretório "novo-diretorio" recém-criado
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")



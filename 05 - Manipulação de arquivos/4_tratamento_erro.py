from pathlib import Path

# Obtendo o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

try:
    # Tentando abrir o arquivo "novo.txt" dentro do diretório "novo-diretorio"
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    # Se o arquivo não for encontrado, exibir mensagem de erro específica
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    # Se o caminho especificado for um diretório em vez de um arquivo, exibir mensagem de erro específica
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    # Se ocorrer um erro de E/S (Input/Output), exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    # Se ocorrer qualquer outro tipo de exceção não prevista, exibir uma mensagem genérica de erro
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

from pathlib import Path

# Obtendo o diretório pai do arquivo atual
ROOT_PATH = Path(__file__).parent

try:
    # Tentando abrir o arquivo "1lorem.txt" para leitura
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        # Lendo e imprimindo o conteúdo do arquivo
        print(arquivo.read())
except IOError as exc:
    # Se ocorrer um erro de E/S (Input/Output), exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo {exc}")

try:
    # Tentando criar e escrever em um arquivo chamado "arquivo-utf-8.txt" com codificação UTF-8
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
except IOError as exc:
    # Se ocorrer um erro de E/S (Input/Output), exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo {exc}")

try:
    # Tentando abrir o arquivo "arquivo-utf-8.txt" para leitura com codificação ASCII
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        # Lendo e imprimindo o conteúdo do arquivo
        print(arquivo.read())
except IOError as exc:
    # Se ocorrer um erro de E/S (Input/Output), exibir mensagem de erro específica
    print(f"Erro ao abrir o arquivo {exc}")

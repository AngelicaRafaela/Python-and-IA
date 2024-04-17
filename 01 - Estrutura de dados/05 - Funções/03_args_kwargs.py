def exibir_poema(data_extenso, *args, **kwargs):
    # Une os argumentos de texto em uma única string, separando-os com uma quebra de linha
    texto = "\n".join(args)
    
    # Cria uma string formatada com os metadados fornecidos
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    
    # Combina a data, o texto e os metadados em uma mensagem formatada, cada chave e valor é separado por uma quebra de linha
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
    # Imprime a mensagem
    print(mensagem)


# Chamada da função com a exibição de um poema e metadados adicionais
exibir_poema(
    "Quarta-feira, 17 de abril de 2024",  # data_extenso
    ("Zen of Python",),  # texto (tupla de um elemento)
    ("Beautiful is better than ugly.",),  # Primeiro verso (tupla de um elemento)
    ("Explicit is better than implicit.",),  # Segundo verso (tupla de um elemento)
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",  # meta_dados
    ano=1999,  # meta_dados
)

from datetime import date, datetime, time

# Criando e imprimindo objetos de data
data = date(2023, 7, 10)  # Cria um objeto date representando a data 10 de julho de 2023
print(data)  # Imprime a data criada
print(date.today())  # Imprime a data atual usando o método today() do objeto date

# Criando e imprimindo objetos de data e hora
data_hora = datetime(2023, 7, 10, 10, 30, 20)  # Cria um objeto datetime representando a data e hora 10 de julho de 2023, 10:30:20
print(data_hora)  # Imprime a data e hora criada
print(datetime.today())  # Imprime a data e hora atuais usando o método today() do objeto datetime

# Criando e imprimindo objetos de hora
hora = time(10, 20, 0)  # Cria um objeto time representando a hora 10:20:00
print(hora)  # Imprime a hora criada

nome = "Angelica"
idade = 31
profissao = "Programador"
linguagem = "Python"
saldo = 45.535

dados = {"nome": "Angelica", "idade": 28, "saldo": 45.535}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {name} Idade: {age} {name} {name} {age}".format(name=nome, age=idade))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:0.2f}")
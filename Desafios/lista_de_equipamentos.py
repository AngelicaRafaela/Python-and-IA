# Crie uma Lista para armazenar os equipamentos
equipamentos = []

# Loop para solicitar ao usuário inserir até três equipamentos
for i in range(3):
    equipamento = input("Digite o nome do equipamento: ")
    equipamentos.append(equipamento)

# Exibe a lista de equipamentos
print("Lista de Equipamentos:")
for equipamento in equipamentos:
    print(f"- {equipamento}")

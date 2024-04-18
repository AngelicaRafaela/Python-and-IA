def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif 10 < consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

consumo = float(input("Digite o consumo médio mensal de dados em GB: "))
print(recomendar_plano(consumo))
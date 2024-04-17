salario = 2000  # Definindo a variável global 'salario' com o valor 2000

def salario_bonus(bonus):  # Definindo a função 'salario_bonus' que recebe um parâmetro 'bonus'
    global salario  # Declarando que a variável 'salario' é global, permitindo que seja modificada dentro da função
    
    lista_aux = lista.copy()  # Criando uma cópia da lista global 'lista' e armazenando em 'lista_aux'
    lista_aux.append(2)  # Adicionando o valor 2 à lista_aux
    print(f"Lista aux = {lista_aux}")  # Imprimindo a lista_aux
    
    salario += bonus  # Adicionando o 'bonus' ao 'salario' global
    return salario  # Retornando o novo valor do 'salario'

lista = [1]  # Definindo a lista global 'lista' com o valor [1]
salario_com_bonus = salario_bonus(500)  # Chamando a função 'salario_bonus' com o argumento 500, retornando o novo valor do 'salario' com o bônus
print("R$", salario_com_bonus)  # Imprimindo o novo 'salario' com o bônus
print(lista)  # Imprimindo a lista global 'lista' após a chamada da função

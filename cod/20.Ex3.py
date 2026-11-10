# Implemente um programa que receba as temperaturas médias registradas durante 
# os 7 dias da semana (armazenadas em um vetor de números reais). 
# O programa deve calcular a média aritmética semanal e, em seguida, 
# exibir quais temperaturas registradas ficaram estritamente abaixo dessa média.

lista = []

for i in range(7):
    temperatura = float(input(f'Digite a média do {i+1}º dia: '))
    lista.append(temperatura)

media_temperatura = sum(lista) / len(lista) 

for temperatura in lista:
    if temperatura < media_temperatura:
        print(temperatura)
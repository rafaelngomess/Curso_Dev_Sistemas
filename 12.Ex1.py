# usuário digitará dez números inteiros para preencher um vetor. 
# Em seguida, o programa deve percorrer o vetor e 
# substituir todos os números negativos por zero, exibindo o vetor final na tela.

numeros = []
for i in range(0, 4):
    num = int(input('Digite um numero: '))
    numeros.append(num)

# Forma 1 -> For each (para cada)
# a ideia é ver o valor de cada posição da lista
for num in numeros:
    # [0, 1, 9, -5, 8]
    # numeros[9] -> da errado
    # descobrir quem é o numero negativo
    if num < 0:
        # saber qual a posição do negativo
        indice = numeros.index(num)
        # numeros[numeros.index(num)] = 0
        # substituir por 0
        numeros.remove(num)
        # numeros.pop(indice) # outra forma
        numeros.insert(indice, 0)


# Forma 2 -> FOR padrão (verifica a posição)
for i in range(0, len(numeros)):
    # [0, 1, 9, -5, 8]
    if numeros[i] < 0:
        numeros[i] = 0

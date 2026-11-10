matriz = []
for i in range(3): # 3 linhas
    linha = [] # inicia a linha vazia
    for j in range(3): # 3 colunas
        numero = int(input('Digite um número entre 1 e 9: '))
        # garantir que não tenha numeros fora do intervalo 1~9
        while numero < 1 or numero > 9:
            numero = int(input('Digite um número entre 1 e 9: '))

        linha.append(numero) # guarda o numero na linha

    matriz.append(linha) # adiciona a linha completa a matriz

# validar as linhas/Matriz
# reescrever como um vetor/lista
valores = []
for i in range(3):
    for j in range(3):
        valores = matriz[i][j] 
# ordenar todos os valores
valores_ordenados = sorted(valores)
# verificar se estão dentro dos limites (1 ~ 9)
valores_validos = valores_ordenados == list(range(0, 10))
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# contador = 0
# for i in range(len(valores_ordenados)):
#     if valores_ordenados[i] == lista[i]:
#         contador += 1
# -----------------------------------------------------------
# reescrevendo as linhas acima
valores = [matriz[i][j] for i in range(3) for j in range(3)]
valores_validos = sorted(valores) == list(range(1, 10))
# -----------------------------------------------------------
# Forma 2 - Lógica

# fazer verificações

somas = [
    matriz[0][0] + matriz[0][1] + matriz[0][2], # linha 1
    matriz[1][0] + matriz[1][1] + matriz[1][2], # linha 2
    matriz[2][0] + matriz[2][1] + matriz[2][2], # linha 3
    matriz[0][0] + matriz[1][0] + matriz[2][0], # coluna 1
    matriz[0][1] + matriz[1][1] + matriz[2][1], # coluna 2
    matriz[0][2] + matriz[1][2] + matriz[2][2], # coluna 3
    matriz[0][0] + matriz[1][1] + matriz[2][2], # diagonal 1
    matriz[0][2] + matriz[1][1] + matriz[2][0] # diagonal 2
]

# verificar "tudo"
if valores_validos and all(soma == 15 for soma in somas):
    print('É um quadrado mágico, e tu acertou')
else:
    print('Errou, pq não tem magia')
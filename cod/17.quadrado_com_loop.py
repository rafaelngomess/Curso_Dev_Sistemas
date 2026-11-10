matriz = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4]
]

soma_diag1 = 0
soma_diag2 = 0
somas = []

for i in range(3):
    soma_linha = 0
    soma_coluna = 0
    for j in range(3):
        soma_linha += matriz[i][j]   # Soma elementos da linha i
        soma_coluna += matriz[j][i]  # Soma elementos da coluna i
    
    # Acumula diagonais a cada passo do laço externo
    soma_diag1 += matriz[i][i]
    soma_diag2 += matriz[i][2 - i]
    
    # Registra a linha e a coluna calculadas nesta iteração
    somas.append(soma_linha)
    somas.append(soma_coluna)

# As diagonais só podem ser apensadas após o término completo das 3 iterações
somas.append(soma_diag1)
somas.append(soma_diag2)

# Validação: todas as 8 somas computadas devem convergir para 15
if all(s == 15 for s in somas):
    print("Quadrado mágico válido.")
else:
    print("Não é um quadrado mágico.")
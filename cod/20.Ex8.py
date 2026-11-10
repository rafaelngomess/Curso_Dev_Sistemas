# O programa deve preencher duas listas paralelas de tamanho fixo 
# (6 posições): uma contendo o código numérico de cada produto e 
# outra contendo o respectivo saldo em estoque.
cod_numerico = []
saldo_estoque = []

for i in range(6):
    codigo = int(input('Digite o codigo numerico do produto '))
    saldo = int(input('Digite o saldo desse produto: '))
    cod_numerico.append(codigo)
    saldo_estoque.append(saldo)

# Solicite ao operador o valor do "Estoque Mínimo de Segurança" 
# (um número inteiro único para a verificação de toda a linha).
estoque_minimo = int(input('Informe o valor mínimo de estoque: '))

# Realize uma varredura nas estruturas e identifique:
indice_menor = 0
indice_maior = 0
contador = 0
for i in range(6):
    # Quais produtos estão com saldo estritamente abaixo do estoque mínimo, 
    # exibindo seu código e quantidade atual;
    if saldo_estoque[i] < estoque_minimo:
        print(f'Código {cod_numerico[i]} - Saldo Atual {saldo_estoque[i]}')
        contador += 1

    # achar o maior - verifica se a posição da lista tem maior quantidade do
    # que o maior anterior
    if saldo_estoque[i] > saldo_estoque[indice_maior]:
        indice_maior = i
    # achar o menor - verifica se a posição da lista tem menor quantidade do
    # que o menor anterior
    if saldo_estoque[i] < saldo_estoque[indice_menor]:
        indice_menor = i

print(f'O produto com menor saldo tem o código {cod_numerico[indice_menor]} e \
      saldo igual {saldo_estoque[indice_menor]}')

print(f'O produto com maior saldo tem o código {cod_numerico[indice_maior]} e \
      saldo igual {saldo_estoque[indice_maior]}')

if contador == 0:
    print('Estoque Operando em Parâmetros Normais')
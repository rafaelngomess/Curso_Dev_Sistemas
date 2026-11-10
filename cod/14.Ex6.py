# usuário digitará o nome e o bairro de dez pessoas. 
# O programa exibirá o nome e bairro das pessoas 
# em ordem alfabética.

cadastro = []
for i in range(4):
    nome = input('Digite o nome: ')
    bairro = input('Digite o bairro: ')
    cadastro.append([nome, bairro])
    # cadastro[i] = [nome, bairro]

# Opção 1 -> Ordernar pelo nome
cadastro.sort()

# Opção 2 -> Ordernar pelo bairro
cadastro.sort(key=lambda x: x[1])
# usuário digitará o nome e a média de dez alunos e o 
# programa escreverá, na tela, o nome de todos com a 
# média acima ou igual a seis.

lista = []
for i in range(0, 4):
    aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite a média do aluno: '))
    lista.append([aluno, nota])

# versão foreach
for aluno_nota in lista:
    if aluno_nota[1] >= 6:
        print(aluno_nota[0])

# versão for padrão
for i in range(0, len(lista)):
    if lista[i][1] >= 6:
        print(lista[i][0])

# versão pythones (compreensão de listas)
nomes = [aluno[0] for aluno in lista if aluno[1] >= 6]
print(nomes)
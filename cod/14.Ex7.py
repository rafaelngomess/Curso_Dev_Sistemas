# o usuário digitará o nome e a média de cinco alunos e 
# o programa só aceitará a média
# do aluno caso ela esteja entre zero e dez.

lista = []
for i in range(5):
    nome = input('Digite o nome: ')
    media = float(input('Digite a média: '))
    while media < 0 or media > 10:
        media = float(input('Tu errou! Digite a média: '))
    lista.append([nome, media])

        

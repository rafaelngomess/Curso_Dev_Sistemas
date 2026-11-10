# 1º passo: pegar duas notas
# 2º passo: fazer a média
# 3º passo: verificar se a média é menor que 6

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 6:
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado')
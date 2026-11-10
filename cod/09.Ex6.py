# usuario digita uma nota
# programa verifica e só aceita se estiver
# entre 0 e 10, caso contrario, peça para 
# digitar de novo

nota = float(input('Digite a nota: '))
# while(0 < nota > 10):
while(nota < 0 or nota > 10):
    print(f'Você digitou {nota}')
    nota = float(
        input('Digite a nota entre 0 e 10: '))


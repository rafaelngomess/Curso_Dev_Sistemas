# pc sorteia numero entre 1 e 50
# tu tem 5 chances de acertar
import random

print('Bem vindo(a) ao jogo de adivinhação')
pontos = 0
for i in range(3):
    print(f'Essa é sua {i+1}ª rodada')
    numero_aleatorio = random.randint(1, 50)
    tentativas = 0 # numero de chances
    acertou = False # variavel de controle
    # enquanto tiver chances
    while tentativas < 5:
        palpite = int(input('Dê seu chute (1 à 50): '))

        # se acertou
        if palpite == numero_aleatorio:
            print('Você acertou Miseraví!')
            acertou = True
            if tentativas == 4:
                pontos += 10
            else:
                pontos += (100 - tentativas*25)

            break # para a execução do laço While

        # ajudas
        elif palpite < numero_aleatorio:
            print('Tente um número maior')

        elif palpite > numero_aleatorio:
            print('Tente um número menor')

        tentativas += 1 # usou uma tentativa

    if not acertou:
        print(f'Nessa rodada ({i+1}), você errou muito, gastou tudo')
        print(f'O número aleatório era: {numero_aleatorio}\n\n')

if pontos >= 200:
    print(f'Sabe muito, faturou {pontos} pontos')
elif 100 < pontos < 200:
    print(f'Até que tu sabe algo, {pontos} pontos para tu')
else:
    print(f'Tente de novo, ou não, só {pontos} pontos')
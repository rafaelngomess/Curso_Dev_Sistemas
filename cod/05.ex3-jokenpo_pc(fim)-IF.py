import random
jogador = input('Pedra, Papel ou Tesoura: ').lower()
# jogador = jogador.lower()
jogadas = ['pedra', 'papel', 'tesoura']

pc = random.choice(jogadas)
print(pc)
if (jogador not in jogadas 
    or pc not in jogadas):
    print('Jogada Invalida')

elif jogador == pc:
    print('Empate')
elif ( (jogador == 'papel' and pc == 'pedra') 
    or (jogador == 'pedra' and pc == 'tesoura')
    or (jogador == 'tesoura' and pc == 'papel') 
    ):
    print('Jogador Ganhou!')
else:
    print('PC Ganhou!')
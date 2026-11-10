# pensar em quem e quando ganha

jogador1 = input('Pedra, Papel ou Tesoura: ')
jogador2 = input('Pedra, Papel ou Tesoura: ')
jogadas = ['Pedra', 'Papel', 'Tesoura']
# quando ninguem ganha -> empate
# empate = jogador1 == jogador2

if (jogador1 not in jogadas 
    or jogador2 not in jogadas):
    print('Jogada Invalida')

elif jogador1 == jogador2:
    print('Empate')
# quando o jogador1 ganha?
# (Papel, Pedra), (Pedra, Tesoura), (Tesoura, Papel)
elif ( (jogador1 == 'Papel' and jogador2 == 'Pedra') 
    or (jogador1 == 'Pedra' and jogador2 == 'Tesoura')
    or (jogador1 == 'Tesoura' and jogador2 == 'Papel') 
    ):
    print('Jogador 1 Ganhou!')
# else -> jogador2 ganhou
else:
    print('Jogador 2 Ganhou!')
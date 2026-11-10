# Construa um jogo de pedra, papel e tesoura.

jogador1 = input('Pedra, Papel ou Tesoura: ')
jogador2 = input('Pedra, Papel ou Tesoura: ')

# primeiro bloco -> jogador1 == Pedra
if (jogador1 == 'Pedra'):
    if(jogador2 == 'Pedra'):
        print('Empate')
    if(jogador2 == 'Papel'):
        print('Jogador 2 Ganhou!')
    if(jogador2 == 'Tesoura'):
        print('Jogador 1 Ganhou!')

# segundo bloco -> jogador1 == Papel
if jogador1 == 'Papel':
    if jogador2 == 'Pedra':
        print('Jogador 1 Ganhou!')
    if jogador2 == 'Papel':
        print('Empate')
    if jogador2 == 'Tesoura':
        print('Jogador 2 Ganhou!')

# terceiro bloco -> jogador1 == Tesoura
if jogador1 == 'Tesoura':
    if jogador2 == 'Pedra':
        print('Jogador 2 Ganhou!')
    if jogador2 == 'Papel':
        print('Jogador 1 Ganhou!')
    if jogador2 == 'Tesoura':
        print('Empate')
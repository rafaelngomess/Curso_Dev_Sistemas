garagem = [['Land Rover', 2014], 
           ['Ora 5', 2026],
           ['Volkswagen', 1963], # [2][1]
           ['Palio', 1997],
           ['Fiat Uno', 2002], # [4][0]
           ['Nissan Sentra', 2016]]

garagem[4] = ['Vectra', 1999]
for carro in garagem:
    print(f'{carro[0]}, ano {carro[1]}')
    # print(carro)

# modificar um dos carros
# for i in range(0, len(garagem)):
#     if i == 0:
#         garagem[i][0] = 'Ferrari F430 Spider'
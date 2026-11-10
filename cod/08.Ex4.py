#digitar um numero 
# criar a tabuada do numero até 10

numero = int(input('fale a tabuada que tu quer aprender: '))

for i in range(0, 10):
    resultado = numero * (i + 1)
    print(f'{numero} * {i+1} = {resultado}')

i = 0
while(i <= 10):
    print(f'{numero} * {i} = {i*numero} ')
    i+=1
    
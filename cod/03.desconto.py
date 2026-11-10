salario = 1000
# desconto inicial
desconto = 0
print(desconto)

# desconto da passagem
passagem = 6/100 * salario
desconto = passagem
print(desconto) #60

# desconto do VR
vr = 2/100 * salario
desconto = desconto + vr
desconto += vr
print(desconto)
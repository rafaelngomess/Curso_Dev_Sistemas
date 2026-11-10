# 1 Passo -> Receber 3 numeros
# 2 Passo -> Verificar a soma dos lados
# 3 Passo -> Se for triangulo, classificar o tipo
# 4 Passo -> Erro se não for triangulo

lado_a = float(input('Digite o lado A: '))
lado_b = float(input('Digite o lado B: '))
lado_c = float(input('Digite o lado C: '))

condicao = (
    (lado_a + lado_b > lado_c) and
    (lado_a + lado_c > lado_b) and
    (lado_b + lado_c > lado_a)
)

if condicao:
    if lado_a == lado_b == lado_c:
        print('Equilatero')

    elif lado_a != lado_b != lado_c:
        print('Escaleno')

    elif (lado_a == lado_b  or 
          lado_a == lado_c or lado_b == lado_c):
        print('Isosceles')

else:
    print('Não é um triangulo')
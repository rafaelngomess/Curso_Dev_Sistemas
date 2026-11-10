# somar 2 numeros
def somar(a, b):
    a = a + b # esse 'a' só existe dentro do escopo da função
    return a # isso faz ser uma função

a = 5 # esse 'a' aqui não é o mesmo da função
b = 4
c = somar(b, a) # 4, 5 
# parametros são posicionais, eles não olham os nomes
print(c)
print(a)


# subtrair 2 numeros
def subtrair(a, b):
    '''
    Essa função subtrai o 'a' de 'b' e retorna o valor
    '''
    return a - b

# subtrair()

# saber se é impar
def impar(numero):
    if not numero % 2 == 0:
        return True

    return False

def impar2(numero):
    return not numero % 2 == 0


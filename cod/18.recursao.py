# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Recursão

# 5! = ? -> 120
# 5 * 4! = ? -> 5 * 24 = 120
# 4 * 3! = ? -> 4 * 6 = 24
# 3 * 2! = ? -> 3 * 2 = 6
# 2 * 1! = ? -> 2 * 1 = 2
# 1 * 0! -> 0! = 1 -> 1 * 1 = 1

def fatorial(numero):
    if numero <= 1:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(-1))

# fibo
# proximo = atual + anterior
# numero = (numero - 1) + (numero - 2)
def fibonacci(numero):
    if numero <= 1:
        return numero
    return (fibonacci(numero - 1) + 
            fibonacci(numero - 2))

print(fibonacci(20))
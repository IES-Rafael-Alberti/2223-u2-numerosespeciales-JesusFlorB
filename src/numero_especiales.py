def sumar_pares(numero_inicial, numero_final):
    suma = 0
    for i in range(numero_inicial, numero_final+1, 10):
        if i % 2 == 0 and i % 3 != 0:
            suma += i
    return suma

def sumar_impares(numero_inicial, numero_final):
    suma = 0
    for i in range(numero_inicial, numero_final+1, 10):
        if i % 2 != 0 and i % 3 != 0:
            suma += i
    return suma

numero_inicial = 10
numero_final = 100
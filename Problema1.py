
"""
Cree un proyecto en Python donde cree un arreglo de int de un tamaño indicado por el usuario y se llene con números aleatorios de entre 2 a 4 cifras. Cree una función recursiva que indique el promedio entre el máximo y mínimo valor del arreglo tal que sean múltiplos de 3.
Por ejemplo si se tiene [5, 6, 10, 9, 12, 14] -> resultado = (12+6)/2 = 9

"""
import random

def promedioMult3(lst):
    ult = len(lst) - 1
    return promMult3(lst, ult, None, None)

def promMult3(lst, pos, mayor, menor):
    if pos == -1:
        return (mayor + menor) / 2
    else:
        if lst[pos] % 3 == 0:
            mayor = lst[pos] if mayor == None or lst[pos] > mayor else mayor
            menor = lst[pos] if menor == None or lst[pos] < menor else menor
        return promMult3(lst, pos - 1, mayor, menor)

tam = int(input("Por favor, ingrese tamaño del arreglo: "))

lista = []

for i in range(tam):
    lista.append(random.randint(10, 9999))

print(f"la lista generada fue: {lista}")

print(f"el promedio es: {promedioMult3(lista)}")
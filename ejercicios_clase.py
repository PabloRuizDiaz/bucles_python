#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pablo Ruiz Diaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.2"

condicion = False


def ej1():
    # Ejercicios con bucles "while"
    
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración

    x = 0
    
    print('Ejercicio 1 - 1er WHILE')

    while not condicion:     # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        if x < 6:
            x += 1           # Coloque la línea de código para que "X" incremente "1"
            continue
        break
    
    # Inove: La resolución del problema anterior es válida, pero existe una forma
    # resolverlo sin tener que utilizar continuo o break ya que la condición es conocida
    # y no alterable
    x = 0
    while x < 6:     # "condicion" reemplazada por "x < 6"
        print("Valor de x =", x)
        x += 1           # Coloque la línea de código para que "X" incremente "1"
    
    
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    x = 5

    print('\nEjercicio 1 - 2do WHILE')

    while not condicion:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        if x >= 0:
            x -= 1
            continue
        break
        # Coloque la línea de código para que "X" decremente "1"


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']

    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...

    print('\nEjercicio 2 - 1er FOR')

    for color in colores:
        print(color)

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...

    print('\nEjercicio 2 - 2do FOR')

    for i in range(len(colores)):
        print(colores[i])


def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero

    print('\nEjercicio 3')

    for i in range(len(numeros)):
        suma += numeros[i]

    print('La suma de todos los valores de la lista "numeros" es {}' .format(suma))


def ej4():
    # Ejercicios con bucles "while"

    x = 0
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    print('\nEjercicio 4 - A)')

    while (x < 10 and x != 6):
        print('El valor de x es ', x)
        x += 2

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    print('\nEjercicio 4 - B)')

    x = 0

    while x < 10:
        if x == 6:
            break
    
        print('El valor de x es', x)
        x += 2

def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))
    
    suma = 0

    for i in range(inicio,fin+1):
        suma += i

    print('La sumatoria es', suma)


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    # Imprimir el valor de la cantidad de números positivos y negativos
    
    print('\nEjercicio 6')
    
    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))
    
    cant_num_pos = 0
    cant_num_neg = 0
    
    listas = range(inicio, fin + 1)
    
    for i in listas:
        if listas[i] < 0:
            cant_num_neg += 1
        else:
            cant_num_pos += 1
    
    print('Cantidad de numeros negativos {} y positivos {}' .format(cant_num_neg, cant_num_pos))

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()

#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pablo Ruiz Diaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!\n')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    cuenta = 0
    sumatoria = 0
    
    inicio = int(input('Ingrese 1er numero de la secuencia:\n'))
    fin = int(input('Ingrese ultimo numero de la secuencia:\n'))

    numeros = range(inicio, fin + 1)

    for i in range(len(numeros)):
        cuenta += 1
        sumatoria += numeros[i]

    print('\nCantidad de numeros en la lista {}, y su sumatoria es {}' .format(cuenta, sumatoria))

def ej2():
    print("\nMi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    
    while True:
        numero_1 = float(input('Ingrese el primer número:\n'))
        numero_2 = float(input('Ingrese el segundo número:\n'))
        operacion = str(input('Ingrese la operacion a ejecutar:\n + -> suma \n - -> resta \n * -> multiplicacion \n / -> division \n ** -> potenciacion \n Fin -> Finaliza operacion \n'))

        if operacion == 'Fin':
            break
        elif operacion == '+':
            print('La suma es {}' .format(numero_1 + numero_2))
        elif operacion == '-':
            print('La resta es {}' .format(numero_1 - numero_2))
        elif operacion == '*':
            print('La multiplicacion es {}' .format(numero_1 * numero_2))
        elif operacion == '/':
            print('La division es {}' .format(numero_1 / numero_2))
        elif operacion == '**':
            print('{} a la potencia de {} es {}' .format(numero_1, numero_2, numero_1 ** numero_2))
        else:
            print('ERROR: Operacion matematica no existente.')


def ej3():
    print("\nMi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe calcular el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    sumatoria = 0
    cantidad_notas = 0 
    cantidad_ausentes = 0

    for nota in notas:
        if nota >= 0:
            sumatoria += nota
            cantidad_notas += 1
        else:
            cantidad_ausentes += 1

    puntaje = sumatoria / cantidad_notas   #puntaje promedio de notas

    print('El alumno tiene {} examenes rendidos y {} ausentes' .format(cantidad_notas, cantidad_ausentes))
    print('La nota final promedio es:')

    if puntaje >= 60:
        if puntaje >= 70:
            if puntaje >= 80:
                if puntaje >= 90:
                    print('A')
                else:
                    print('B')
            else:
                print('C')
        else:
            print('D')
    else:
        print('F')

def ej4():
    print("\nMi primer pasito en data analytics")

    '''
    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    #temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    for x in temp_dataloger:
        if (temperatura_max is None or temperatura_max < x):
            temperatura_max = x
        
        if (temperatura_min is None or temperatura_min > x):
            temperatura_min = x
        
        temperatura_sumatoria += x
    
    temperatura_promedio = temperatura_sumatoria / len(temp_dataloger)

    print('\nTemperatura max {} y min {}. Con un promedio de {}' .format(temperatura_max, temperatura_min, temperatura_promedio))
 
    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    print('\nPor Python')

    temperatura_max = max(temp_dataloger)
    temperatura_min = min(temp_dataloger)
    temperatura_promedio = sum(temp_dataloger) / len(temp_dataloger)

    print('\nTemperatura max {} y min {}. Con un promedio de {}' .format(temperatura_max, temperatura_min, temperatura_promedio))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    verano = [19,28]
    otono = [11,24]
    invierno = [8,14]
    primavera = [10,24]

    #Las estaciones se organizaron en referencia de menor a mayor en temperaturas minimas,
    #y comparando si el rango esta dentro de cada rango promedio por estacion
    #Esta analogia tiene el problema que otono y primavera son parecidos,
    #por lo que deberia de juntarse algun dato mas como humedad para ser mas precisos.

    if temperatura_min >= min(invierno) and temperatura_max <= max(invierno):
        print('Invierno')
    elif temperatura_min >= min(primavera) and temperatura_max <= max(primavera):
        print('Primavera')
    elif temperatura_min >= min(otono) and temperatura_max <= max(otono):
        print('Otono')
    else:
        print('Verano')

def ej5():
    print("\nAhora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''

    while True:
        i = 0
        palabras = []
        palabras_max = []
        palabras_largo_max = []

        operacion_txt = str(input('Ingrese accion a realizar: \n 1 -> Orden alfabetico \n 2 -> Cantidad de letras \n 3 -> Finalizar \n'))

        if operacion_txt == '3':
            break
        elif operacion_txt != '1' and operacion_txt != '2':
            print('ERROR: Operacion no valida.\n')
            continue
        
        while True:
            palabra = str(input('Ingrese palabra (para finalizar escriba *):\n'))
            
            if palabra == '*':
                break
            
            palabras.append(palabra)
            
        copy_palabras = palabras

        if operacion_txt == '1':
            for i in range(len(palabras)):
                palabra_max = None
                for palabra in copy_palabras:
                    if (palabra_max is None or palabra_max < palabra):
                        palabra_max = palabra
                palabras_max.append(palabra_max)
                copy_palabras.remove(palabra_max)
            print('Orden alfabetico\n {}' .format(palabras_max))
        elif operacion_txt == '2':
            for i in range(len(palabras)):
                palabra_max = None
                largo_max = None
                for palabra in copy_palabras:
                    if (largo_max is None or largo_max < len(palabra)):
                        largo_max = len(palabra)
                        palabra_max = palabra
                palabras_largo_max.append(largo_max)
                copy_palabras.remove(palabra_max)
            print('Orden de largo\n {}' .format(palabras_largo_max))

    print('Finalizado')
 
if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()

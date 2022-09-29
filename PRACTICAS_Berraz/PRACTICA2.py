#Práctica de introducción a Python - Parte 2

#alternativa condicional

#ejercicio 1: creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

cadena_por_teclado = input("Cadena: ")
if cadena_por_teclado[0] == cadena_por_teclado[0].upper:
    print("la primer letra es mayuscula")
else:
    print("la primer letra es minuscula")


#ejercicio2: escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

numero = int(input("insertar numero: "))
numero_par = (numero % 2) == 0
numero_impar = (numero % 2) != 0
numero_positivo = numero > 0
numero_negativo = numero < 0
if numero_par and numero_positivo:
    print("el numero es positivo y par")
elif numero_impar and numero_positivo:
    print("el numero es positivo e impar")
elif numero_negativo and numero_par:
    print("el numero es negativo y par")
else:
    print("el numero es negativo e impar")

#ejercicio 3: escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

numero = int(input("ingresar un numero: "))
if numero == 1:
    print("6")
elif numero == 2:
    print("5")
elif numero == 3:
    print(4)
elif numero == 4:
    print("3")
elif numero == 5:
    print("2")
elif numero == 6:
    print("1")
else:
    print("incorrecto el numero ingresado")

#ejercicio 4: realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

zona = int(input("Ingrese la zona de la entrega: "))
gramos= int(input("Peso del paquete en gramos: "))

if gramos < 5000:
    if zona == 1:
        print("El valor de la entrega es de:", gramos * 10)
    elif zona == 2:
        print("El valor de la entrega es de:", gramos * 15)
    elif zona == 3:
        print("El valor de la entrega es de:", gramos * 18)
    elif zona == 4:
        print("El valor de la entrega es de:", gramos * 24)
    elif zona== 5:
        print("El valor de la entrega es de:", gramos * 30)
    else:
        print("No esta dentro de la zona de envios")
else:
    print("Exceso de peso")

#ejercicio 5: creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

numero_dia = int(input("Inserte numero de dia de la semana: "))
if numero_dia <= 7 and numero_dia > 0:
    if numero_dia == 1:
        print("El dia es lunes")
    elif numero_dia == 2:
        print("El dia es martes")
    elif numero_dia == 3:
        print("El dia es miercoles")
    elif numero_dia == 4:
        print("El dia es jueves")
    elif numero_dia == 5:
        print("El dia es viernes")
    elif numero_dia == 6:
        print("El dia es sabado")
    else:
        print("El dia es domingo")
else:
    print("Numero incorrecto")

#LISTAS


#ejercicio 6: Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

lista1 = input(" 5 caracteres: ")
lista2 = lista1[::-1]
print(lista2)

#ejercicio 7: Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista. 



#ejercicio 8: Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)

lista1 = []
lista2 = []
lista3 = []

for indice in range(5):
    lista1.append(int(input("Introduce un numero entero lista 1: ")))
for indice in range(5):
    lista2.append(int(input("Introduce un numero entero lista 2: ")))
for indice in range(5):
    lista3.append(lista1[indice] + lista2 [indice])
print(lista3)

#ejercicio 9: Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:
                #La edad máxima de todos los alumnos.
                #Los alumnos que tengan la edad máxima

nombres= []
edades = []
while(True):
    nombre = input("Introducir nombre: ")
    if (nombre == "*"):
            break
        
    edad = int(input("introducir edades: "))
    nombres.append(nombre)
    edades.append(edad)

    max = print(max(edades))
    i=0
    for e in edades:
        
        if(e == max):
            print(nombres[i])
        i+=1


    








#DICCIONARIOS
#ejercicio 10: Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

cadena = input("Cadena: ")
apariciones_caracter = {}


for letra in cadena:
    if letra in apariciones_caracter.keys():
        pass

    else:
        cant = cadena.count(letra)
        apariciones_caracter.update({letra: cant})


#ejercicio 11: Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

cadena = input("Cadena: ")
apariciones_caracter = {}


for letra in cadena:
    if letra in apariciones_caracter.keys():
        pass

    elif letra not in apariciones_caracter.keys():
            cant = cadena.count(letra)
            apariciones_caracter.update({letra: cant})
    
    else:
        print letra not in apariciones_caracter


#ejercicio 12: Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.


cant_alumnos = []
nombres= []
notas = []
alumnos_y_notas = { }

cant_alumnos = int(input("Numero de alumnos : "))

for posicion in range(cant_alumnos):
    nombre = input("Nombre: ")

    alumnos_y_notas[nombre]=None

    while(True):
        notas = int(input("Notas : "))
        if (notas < 0):
                break
        else:
            alumnos_y_notas[nombre]+=notas
        








#FUNCIONES
#ejercicio 13: Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.


numeros_enteros = int(input("Introducir dos números enteros: "))

def esMultiplo(numeros_enteros):        
    for numero[0] in numeros_enteros:
        if numero[0] % numero[1] == 0:
            print("Es número entero")
        else:
            print("No es número entero")

#ejercicio 14: Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.



cant_dias = int(input("Número de días: "))

def temperatura_media(temperaturas):
    for temperaturas in range(cant_dias):
        print(sum(temperaturas) / cant_dias)

#ejercicio 15: Creá un programa para gestionar datos de los socios de un club.


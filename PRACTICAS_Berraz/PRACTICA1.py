#Práctica de introducción a Python - Parte 1

#ejercicio 1 : escribir un programa que imprima la longitud de un string el cual se lee por teclado.

from telnetlib import SB


def imprimir_longitud (palabra):
    longitud = len(palabra)
    print (longitud)

imprimir_longitud("sofia")


#ejercicio 2: realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

def imprimir_5y6(palabra):
    if len(palabra) > 5:
        quinta = palabra[5].upper() 
        sexta = palabra[6].upper()
        print (quinta)
        print (sexta)
    else: 
        print("la palabra debe tener más caracteres")

imprimir_5y6("manzanilla")
imprimir_5y6("manza")

#ejercicio 3: escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

nombreyapellido = input("Ingresar nombre y apellido: ")
print (f"Hola {nombreyapellido}")


#ejercicio 4: pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas

nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido/s: ")
print (nombre[0].upper(), apellido[0].upper())


#ejercicio 5: realizar un programa que lea tres números por teclado y calcule el promedio de ellos.

numero1 = int(input("Numero 1:"))
numero2 = int(input("Numero 2:"))
numero3 = int(input("Numero 3:"))
print((numero1 + numero2 +numero3)/ 3)


#ejercicio 6: dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

minutos = int(input("Minutos: "))
horas = minutos/60
resto = minutos%60
print(f"Son {horas} horas y {resto} minutos ")



#ejercicio 7: Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

sueldo_base = int(input("Sueldo: "))
comision = (sueldo_base * 0.10)
comision_cuatro_ventas = (comision * 4)
sueldo_total = int(sueldo_base) + int(comision_cuatro_ventas)
print(sueldo_total)

#ejercicio 8: Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta

q_correctas = int(input("Cantidad de respuestas correctas: "))
q_incorrectas = int(input("Cantidad de respuestas incorrectas: "))
q_en_blanco = int(input("Cantidad de respuestas en blanco: "))
nota_final = 4 * q_correctas - 1 * q_incorrectas 
print(nota_final)


#ejercicio grupal

costo_total= int(input('Valor de la casa: '))
porcentaje_deposito = costo_total/4
cantidad_ahorrada = 0
g = 4
sueldo_anual =int(input('Sueldo anual: '))
porcentaje_ahorrado = int(input('Cuanto queres ahorrar: '))
sueldo_mensual = sueldo_anual/12

ahorro_mensual = sueldo_mensual * (porcentaje_ahorrado / 10)
mes = 0
while porcentaje_deposito > cantidad_ahorrada:
    mes += 1
    cantidad_ahorrada += ahorro_mensual + (cantidad_ahorrada * g / 12)
else:
    print('Tenes que ahorar por', mes, 'meses')

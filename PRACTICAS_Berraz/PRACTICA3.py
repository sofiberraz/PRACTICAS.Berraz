#Practica de Manipulación de archivos

#ejercicio 1: Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

import os, glob

def empieza_con(letra, archivo):
    suma = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ("Hay", suma, "archivos que no empiezan con", letra) 

#ejercicio 2: Escribí un programa que lea un archivo e imprima las primeras n líneas.

def leer_imprimir (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[: primeras_lineas]
    print(*linea)

leer_imprimir ("tejer.txt", 4)

#ejercicio 3: Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def leer_imprimir_ultimas (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[-primeras_lineas:]
    print(linea) 

leer_imprimir_ultimas("tejer.txt", 4)


#ejercicio 4: Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def leer_palabras_imprimir (archivo):
    palabras = 0
    with open (archivo, "r") as file:
        for line in file:
            palabras += 1
            for i in line:
                if i == " ":
                    palabras += 1
    print("la cantidad es:", palabras)
leer_palabras_imprimir("tejer.txt")

str = "Programming is fun"
words = str.split()

print("Words count:", len(words))  

#ejercicio 5: Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

""""
def leer_reemplazar_saltar (archivo):
     with open (archivo, "r") as f, open(salida, "w") as s:
        for line in f:
            s.write(line.replace (letra, letra + "\n"))
leer_reemplazar_saltar("documento", "documento2", f)
"""


#ejercicio 6: Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.


def leer_palabras_imprimir (archivo):
    linea = open("tejer.txt", "r").readlines()[: archivo]
    saltos_de_linea = 0
    with open (archivo, "r") as file:
        for line in file:
            if line == "/n":
                saltos_de_linea += 1

                    
    print("la cantidad de saltos de línea es:", saltos_de_linea)


#ejercicio 7: Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def start_with(letra, archivo):
    count = 0
    with open(archivo,"r") as file:
            for line in file:
                    if (line[0] != letra.lower() or line [0] != letra.upper()):
                        count +=1
    print ("el numero de lineas que no empiezan con", letra, "es", count)
start_with("H", "documento")


#ejercicio 8: Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

nuevo_archivo= []
def guardar_archivos(archivo1, archivo2):
    with open (archivo1, "r") as file: 
        nuevo_archivo.append(archivo1)
    with open (archivo2, "r") as file:
        nuevo_archivo.append(archivo2)
    print (nuevo_archivo)

#ejercicio 9: Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def start_with( archivo):
    cant_palabra = 0
    frecuencia_palabra = cant_palabra / len(archivo)
    with open(archivo,"r") as file:
            for palabra in file:
                    cant_palabra += 1
                    
    print (frecuencia_palabra)

#ejercicio 10: Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
#ejercicio parcial

def unir_txt(carpeta1, nombre):
    os.chdir(carpeta1)
    textos = glob.glob("*.txt")
    with open ("resultado/" + nombre, "a") as salida:
        for archivo in textos:
            with open (archivo, "r") as texto:
                salida.write(texto.read() + "\n")

                
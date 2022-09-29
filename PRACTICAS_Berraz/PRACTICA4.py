#Practica Expresiones Regulares

#Ejercicio 1: Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

import re
def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9.9]",string))
print("el string", "ABCDEaaa1234", "tiene caracteres permitidos?")

print(caracteres_permitidos("ABCDEaaa1234")) 

#Ejercicio 2: Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9.9]",string))
print("el string", "ABCDEaaa1234", "tiene caracteres permitidos?")

print(caracteres_permitidos("ABCDEaaa1234"))

#Ejercicio 3: Creá un programa que verifique las siguientes condiciones:


#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de dos o tres e.

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("a"))

def encontrar_patron (string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:   
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron("he"))
print(encontrar_patron("hheeeeey"))

#Ejercicio 4: Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$" # el mas es que aparezca una o mas veces, el signo peso es para delimitar cuando termina y el piquito para arriba onde empieza.
    if re.search(patron,string) is not None:
        return "patron encontrado"
    else:
        return "Patron no encontrado"
print(palabras_unidas("aaab_bagdad"))

def palabras_unidas(string):
    patron = "[a-z]+\.+.+[a-z]+"

#Ejercicio 5: Escribí un programa que diga si un string empieza con un número específico.

def numero_especifico(numero, string):
    if re.match(str(numero), string) is not None:
        return "Empieza con el numero"
    else:
        return "NO empieza con el numero"
print(numero_especifico(5, "5sdfgf"))


#Ejercicio 6: Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

def frase_dada(string):
    list = ["a","b","c","d"]
    if re.match(list(), string) is not None:
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(frase_dada("a", "Holacamila"))

#Ejercicio 7: Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def encuentro_string(string):
    patron = ["[a-zA-Z0-9.9]"]
    if re.match(patron, string) is not None: 
        return "Se encuentran en la frase"
    else:
        return "NO se encuentran en la frase"
print(encuentro_string("a", "Holacamila"))

#Ejercicio 8: Escribí un programa que separe y devuelva los caracteres númericos de un string.



#Ejercicio 9: Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")



#Ejercicio 10: Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

#Ejercicio 11: Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).



#Ejercicio 12: Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).



#Ejercicio 13: Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.



#Ejercicio 14: Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.



#Ejercicio 15: Realizá un programa que validar si una cuenta de mail está escrita correctamente.
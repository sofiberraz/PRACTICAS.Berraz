#Practica Programación Orientada a Objetos

#ejercicio 1: Dada la siguiente clase, identificá la interfaz y el estado de la misma:

from email.errors import MalformedHeaderDefect
from importlib.util import module_for_loader


class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2 


""" Los mensajes determinan lo que se conoce como interfaz. (conjunto de mensajes que entiende el objeto)
ESTADO de una clase = INTERFAZ de una clase
POLIMORFISMO: una tercera clase pueda  utilizar indistintamente a dos objetos que compartan interfaz. Cuidador manda mensaje: comer y lo recibe el perro y el gato. Todos entienden ese mensaje.
"""

#ejercicio 2: Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
    def __init__ (self, energia): 
        self.energia = energia 

    def comer_alpiste(self, gramos):
        self.energia = self.energia + 4 * gramos 

    def volar_en_circulos (self):
        self.volar(0)

    def volar(self, kms):
        if(10 + kms < self.energia):
            self.energia -= 10 + kms 
        else: 
            print("No puedo volar esa distancia, no tengo energía")

Camila = Golondrina(100)

Camila.comer_alpiste(50)


#ejercicio 3: Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__ (self, marca, modelo, precio):
     self.marca = marca
     self.modelo = modelo
     self.precio = precio

    def descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * (porcentaje/100))

    def precioACTUAL(self):
        return self.precio 

# instanciar un objeto

notebook1 = Notebook("Asus", "R556L", 8000)

notebook1.descuento(50)
print(notebook1.precioActual())


#ejercicio 4: Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

class Contador:
    def __init__(self, valor):
        self.valor = valor 

    def inc(self):
        self.valor += 1

    def dis(self):
        self.valor -= 1 

    def reset(self):
        self.valor = 0

    def ValorActual(self):
        print(self.valor)

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

"""""inc()

dis()

reset()

valorActual()

valorNuevo(nuevoValor)

Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()"""

#ejercicio 5: Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
    def __init__(self, valor):
        self.valor = valor 
        self.comando = None 

    def inc(self):
        self.valor += 1
        self.comando = "incremento"

    def dis(self):
        self.valor -= 1 
        self.comando = "disminucón"

    def reset(self):
        self.valor = 0
        self.comando = "reset"

    def ValorActual(self):
        print(self.valor)

    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

    def ultimoComando(self, nuevoValor):
        print(self.comando)

#ejercicio 6: Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

class Calculadora:
    def __init__ (self):
        self.valor = None

    def cargar(self, valor):
        self.valor = valor

    def sumar(self, numero):
        self.valor += numero

    def restar(self, numero):
        self.valor -= numero

    def multiplicar(self, numero):
        self.valor *= numero

    def valorActual(self):
        print(self.valor) 
    
    

""""cargar(numero)

sumar(numero)

restar(numero)

multiplicar(numero)

valorActual()

Si se evalúa la siguiente secuencia:

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
el resultado debe ser 24"""

#ejercicio 7: Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrion: 
    def __init__ (self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listGramos = []
        self.listakms = []
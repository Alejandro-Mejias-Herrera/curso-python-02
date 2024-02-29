#Modulos son ficheros que contienen un conjunto de funciones, variables o clases y 
#que pueden ser usados por otros módulos.

#Para preguntar por el sistema operativo
import sys
#Imprime la ubicación en que se está trabajando
print(sys.path)

#módulo de expresiones regulares
import re
text = 'Hola. Mi número de teléfono es 976457845 y el código país es 56'
#Buscamos los números dentro del texto
result = re.findall('[0-9]+',text)
print(result)

import time 
#Devuelve la hora en un formato de la computadora
timestamp = time.time()
print(timestamp)

#Devuelve el tiempo en un formato para las personas
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
#Se obtendrá cada número de la lista con su frecuencia
numbers = [2, 1, 5, 6, 3, 4, 4, 1, 2, 1, 6, 6, 1]
#Devuelve un diccionario con cada valor y su frecuencia
counter = collections.Counter(numbers)
print(counter)


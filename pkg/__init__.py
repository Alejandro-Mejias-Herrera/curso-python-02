#Este archivo se crea para que las versiones anteriores a 3 de Python puedan utilizar los packages
print('Se inició un paquete')

URL = 'platzi.com'

#Para no estar importando las funciones o los módulos 1 por 1, se pueden escribir acá y se importarán de 
#inmediato al utilizar el paquete
import pkg.mod_01, pkg.mod_02

'''
Luego, en el archivo principal se puede escribir 
import pkg
print(pkg.mod_01.function_01())
'''
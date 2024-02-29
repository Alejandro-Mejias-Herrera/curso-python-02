#Un package es una carpeta que contiene varios módulos. Se puede importar completo o sólo parte de él
from pkg.mod_01 import function_01, function_02
from pkg.mod_02 import function_03, function_04


print(function_01())
print(function_02())
print(function_03())
print(function_04())


#Ahora importaremos el módulo arithmetic para hacer operatoria básica
import pkg.arithmetic
#Forma alternativa de importar 
from pkg import arithmetic

print(pkg.arithmetic.add(7,3))
print(pkg.arithmetic.substract(7,3))
print(pkg.arithmetic.product(7,3))
print(pkg.arithmetic.quotient(7,3))

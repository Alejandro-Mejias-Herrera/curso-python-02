#Es frecuente utilizar algunas líneas de código de manera reiterada. En estos casos, 
#conviene escribirlas dentro de una función y luego llamar a la función cuando la necesitemos.

#Escribimos una función que sume dos valores, preguntando ambos al usuario.
a = float(input('Ingrese un primer número '))
b = float(input('Ingrese un segundo número '))

def suma(a, b):
    print(a, ' + ', b, ' = ',a + b)

suma(a,b)
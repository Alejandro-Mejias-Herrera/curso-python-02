import functools

numbers = [0, 1, 4, 9, 16, 25, 36, 49, 64, 100]
suma = 0

#Utilizando for
for number in numbers:
    suma = suma + number

print('Suma con for:', suma)

#Utilizando reduce y una función lambda

suma02 = functools.reduce(lambda counter, item : counter + item, numbers)
print('Suma con reduce:', suma02)

#Utilizando reduce pero sin función lambda

def suma_elementos(counter, item):
    return counter + item

suma03 = functools.reduce(suma_elementos, numbers)
print(suma03)


#Usaremos reduce para obtener el número mayor de una lista

numbers02 = [5, 2, 8, 3, 4, 4, 1, 7]

max_num = functools.reduce(max,numbers02)
print(max_num)

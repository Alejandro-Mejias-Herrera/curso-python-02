#Map es una función que permite utilizar higher order function.
#La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento
#se envía a la función como un parámetro.
#Sintaxis.
#map(function, iterables)
#Se tomará una lista de números y se duplicará cada elemento
#Primero sin map

numbers = [0, 1, 2, 3, 4, 5]
double_numbers = []

for i in numbers:
    double_numbers.append(i*2)

print(numbers)
print(double_numbers)

#Utilizando map

numbers = [0, 1, 2, 3, 4, 5]
double_numbers02 = list(map(lambda x : 2*x, numbers))

print(numbers)
print(double_numbers02)
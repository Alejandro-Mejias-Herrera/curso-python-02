#ITERABLES Un iterable se define como el objeto que contiene un número contable
# con valores y este al tener un valor puede recorrer uno a uno los elementos 
# que la contienen como una estructura de datos y operar con ellos, pero a la vez 
# se rigen bajo la instrucción que se le es dada, con lo cual son dependientes 
# de la instrucción a recibir.

fruits = ['naranja','manzana','durazno','sandía']

#Se puede iterar completamente con un for, pasando por todos los elementos (fruit) de una lista (fruits)
for fruit in fruits:
    print(fruit)

#Se puede usar un for y generando un rango que vaya hasta el lenght de la lista
for i in range (0,len(fruits)):
    print(fruits[i])

#Se puede usar un while. Hay que crear un contador y hacer que vaya aumentando.
count = 0
while count < len(fruits):
    print(fruits[count])
    count += 1

#Se puede hacer con iter, mostrando sólo el siguiente paso. De esa forma, 
#no se tiene que ejecutar el ciclo completo
my_it = iter(fruits)
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
#Se genera un error si nos pasamos del final
print(next(my_it))
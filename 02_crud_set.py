#Conjunto
set_countries = {'Chile', 'Argentina', 'Uruguay', 'Bolivia'}

#Preguntamos la cantidad de elementos que tiene el conjunto
size = len(set_countries)
print(size)

#Preguntar si un elemento está en el conjunto
print('Chile' in set_countries)
print('Perú' in set_countries)

#Agregar un elemento
set_countries.add('Perú')
print(set_countries)

#Agregar cualquier tipo de objeto, como listas, tuplas.
set_countries.update({'Paraguay', 'Colombia'})
print(set_countries)

#Remover elementos
#remove: Si el elemento no se encuentra, arrija error.
#discard: Si el elemento no se encuentra, no arroja nada.
set_countries.remove('Colombia')
print(set_countries)
set_countries.discard('Ecuador')
print(set_countries)

#Para eliminar el primer elemento, que es aleatorio
set_countries.pop()
print(set_countries)

#Para ordenar alfabéticamente los elementos de un conjunto
sorted(set_countries)
print(set_countries)

#Para eliminar todos los elementos
set_countries.clear()
print(set_countries)
print(len(set_countries))
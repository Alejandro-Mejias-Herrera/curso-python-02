#Un conjunto (set) se escribe como un diccionario (llaves), pero no funciona igual. Sólo van los valores.
#Características de un conjunto: Se pueden modificar, no tienen un orden, no admite duplicados.
set_countries = {'Chile', 'Argentina', 'Uruguay', 'Bolivia'}
print(set_countries)
print(type(set_countries))

set_numbers = {2, 3, 5, 7, 11, 13}
print(set_numbers)

#Crea un conjunto a partir de un string. Separa sus elementos.
set_from_string = set('hola')
print(set_from_string)

#Se puede eliminar los valores repetidos de una lista de números transformándolos a un set.
numbers = [2, 6, 4, 2, 5, 6, 2, 7]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
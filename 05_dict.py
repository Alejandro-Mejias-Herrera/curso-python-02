#Crearemos un diccionario de númemros

#De forma lenta
dict_01 = {}
for i in range(1,11):
    dict_01[i] = i*2

print(dict_01)

#Forma rápida
dict_02 = {i : i*2 for i in range(1,11)}
print(dict_02)

#Crearemos un diccionario con países y poblaciones (al azar)

#Forma lenta
import random
countries = ['Argentina', 'Chile','Uruguay','Brasil']
population = {}
for country in countries:
    population[country] = random.randint(50,101)

print(population)

#Forma rápida
import random
countries = ['Argentina', 'Chile','Uruguay','Brasil']
population = {country : random.randint(50,101) for country in countries}
print(population)

#Creamos una lista con nombres y edades. Se muestran tres formas de hacerlo.

names = ['Almendra','Bárbara','Carlos']
ages = [21, 32, 50]

new_dict = {name : age for (name,age) in zip(names,ages)}
print(new_dict)

new_dict02 = {names[i] : ages[i] for i in range(len(names))}
print(new_dict02)

'''
#El código que se muestra a continuación une los datos, pero creando una lista de tuplas. Esa lista se debe traducir a un diccionario o escribir directamente dict(zip(names,ages))
new_list = list(zip(names,ages))
'''

new_dict03 = dict(zip(names,ages))
print(new_dict03)
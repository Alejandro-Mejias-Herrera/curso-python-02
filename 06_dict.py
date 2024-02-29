#Crea un diccionario con países de una lista y le asigna población aleatoria.
import random
countries = ['Chile', 'Argentina', 'Uruguay', 'Brasil', 'Paraguay', 'Perú']
population_countries = {country: random.randint(1,100) for country in countries}
print(population_countries)

#Crea un diccionario con los países cuyas poblaciones sean mayores o iguales a 30 millones
large_populations = {country: population for (country, population) in population_countries.items() if population >= 50}
print(large_populations)

'''
#Crea un diccionario agregando una población previamente establecida
populations = [20, 80, 7, 140, 15, 25]
population_countries2 = {countries[i]: populations[i] for i in range(len(countries))}
print(population_countries2)


#Crea un diccionario agregando sólo las poblaciones mayores o iguales a 30 millones.
large_populations2 = {countries[i]: populations[i] for i in range(len(countries)) if populations[i] >= 50}
print(large_populations2)
'''

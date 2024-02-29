#Cuelquier archivo .py es un módulo, así que se puede importar. 
#También se puede importar sólo una función en vez del archivo entero
#from mod import get_population
import mod
import read_csv
import charts  

#Ejercicio para graficar el porcentaje de población de varios países
def run():
    data = read_csv.read_csv('./app/data.csv')
    #Se aplica un filtro para seleccionar sólo los países de sudamérica.
    data = list(filter(lambda item : item['Continent'] == 'South America', data))
    #Se obtiene la lista de países y sus porcentajes desde los datos utilizando map
    countries = list(map(lambda x : x['Country/Territory'], data))
    percentages = list(map(lambda x : x['World Population Percentage'], data))
    #Se grafica
    charts.generate_pie_chart(countries, percentages)



'''
#Ejercicio para graficar la población de un país a lo latgo del tiempo
#Escribimos todo el procedimiento en una función run(), para que al ser ejecutada desde otro archivo no ejecute
#el código del run. Se debe escribir "main.run() para ejecutarlo"
def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Ingrese el país que desea graficar: ')

    result = mod.population_by_country(data,country)

    if len(result) > 0:
        country = result[0]
        labels, values = mod.get_population(country)
        charts.generate_bar_chart(labels, values)

'''

#Este if es para que si el archivo se ejecuta desde acá, corra la función run(). 
#Si se ejecuta desde otro archivo con un módulo, no entre la la función.
if __name__ == "__main__":
    run()


#Módulo para leer archivos csv
import csv

#Definimos una función que recibirá la ubicación del archivo y lo abrirá
#r implica que tendremos permisos de lectura
def read_csv(path):
    with open(path, 'r') as csvfile:
        #delimiter = ',' implica que en el archivo csv los datos están separados por comas 
        reader = csv.reader(csvfile, delimiter=',')
        #Se guarda en header una lista que tiene los encabezados del csv. Necesitamos unir el encabezado con
        #cada valor
        header = next(reader)
        #Creamos una lista vacía. En esa lista agregaremos diccionarios con clave: valor correspondiente
        #a cada encabezado
        data = []
        print(header)
        for row in reader:
            #Se crea un array de tuplas con pares (encabezado, valor) 
            iterable = zip(header,row)
            #Se puede imprimir para verlo
            #print('***'*5)
            #print(list(iterable))
            #Pero queremos pasarlo a diccionario y luego agregarlo a la lista data
            country_dict = {key:value for key, value in iterable}
            #una forma alternativa para traducir el iterable a un diccionario
            #country_dict = dict(iterable)
            data.append(country_dict)
        return data

#Para correr el archivo como un script desde la terminal
if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data)


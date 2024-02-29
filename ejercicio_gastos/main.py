'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos
de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el 
total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total 
de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y 
el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total 
de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60
'''

import csv

def read_csv(path):
   # Tu código aquí 👇
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter = ',')
      for row in reader:
         total = total + int(row[1])
   return total

response = read_csv('.ejercicio_gastos/data.csv')
print(response)

import csv

def read_csv(path):
   sum = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for data_set in reader:
         sum += int(data_set[1])
   return sum
   
sum_csv = read_csv('.ejercicio_gastos/data.csv')
print(sum_csv)


def read_csv(path):
   with open(path, 'r') as csvfile:      
      total = sum(int(r[1]) for r in csv.reader(csvfile))
      return total

response = read_csv('./data.csv')
print(response)


import csv
import functools

def read_csv(path):
   # Tu código aquí 👇
   with open(path) as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      data = list()
      for line in reader:
         data.append(int(line[1]))
   total = functools.reduce(lambda x,y: x+y, data)
   return total

response = read_csv('.ejercicio_gastos/data.csv')
print(response)
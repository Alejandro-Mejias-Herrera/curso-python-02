#Crearemos una lista de números del 1 al 10.

#Forma lenta
numbers_v1 = []
for element in range(1,11):
    numbers_v1.append(element)

print(numbers_v1)

#Forma rápida
numbers_v2 = [element for element in range(1,11)]
print(numbers_v2)

#Modificación para obtener números pares
#Forma lenta
numbers_v1 = []
for element in range(1,11):
    numbers_v1.append(element*2)

print(numbers_v1)

#Forma rápida
numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)

##Agregar un condicional

#Forma lenta
numbers_v3 = []

for i in range(1,21):
    if i % 5 == 0:
        numbers_v3.append(i*2)

print(numbers_v3)

#Forma rápida
numbers_v4 = [i*2 for i in range(1,21) if i % 5 == 0]
print(numbers_v4)


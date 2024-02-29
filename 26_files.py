#Leemos el archivo completo. Si es corto, no hay problema. Si es largo, puede ocupar mucho espacio de memoria
#r indica que se da permiso de lectura.
#El ecoding utf-8 es para aceptar las tildes
file = open('./text.txt', 'r', encoding='utf-8')
#print(file.read())

#Para leer línea a línea
#print(file.readline())
#print(file.readline())
#print(file.readline())

#Hay que recordar cerrarlo luego de usarlo, para no ocupar memoria de más
#file.close()

#Se puede leer línea a línea con un for. De esa forma, llegamos hasta el final del archivo
for line in file:
    print(line)

file.close()

#Se puede escribir de manera diferente para evitar tener que recordarle que debe cerrarse
with open('./text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)

'''
Enlace para seguir profundizando 
https://realpython.com/working-with-files-in-python/
'''
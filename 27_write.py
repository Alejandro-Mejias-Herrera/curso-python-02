#r+ permite leerlo y luego agregarle nuevas líneas.
#w+ permite leer y escribir, pero sobreescribe el archivo que existe
with open('./text.txt', 'r+', encoding='utf-8') as file:
    for line in file:
        print(line)
    #Agregaremos un par de líneas al archivo
    file.write('\n Una nueva línea de prueba')
    file.write('\n Lo intentaré otra vez')
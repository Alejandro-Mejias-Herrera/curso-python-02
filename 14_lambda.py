#Definimos una función sencilla, que obtendrá el sucesor de un número.
def successor(x):
    return x + 1

n01 = successor(10)
print(n01)

#Usaremos una función lambda o anónima para realizar lo mismo. La sintaxis es de la forma
#nombreFuncion = lambda parámetro : return

successor02 = lambda x : x + 1

n02 = successor02(22)
print(n02)

#Usaremos otra función lambda para crear un nombre completo a partir de un nombre y apellido.
full_name = lambda name, last_name : f'El nombre completo es {name.title()} {last_name.title()}'

text = full_name('Alejandro','mejías herrera')
print(text)



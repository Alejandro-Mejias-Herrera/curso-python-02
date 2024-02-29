#Se aplicará la función map a un diccionario

items = [{
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 300
    },
    {
        'product': 'pantalon2',
        'price': 200
    }
]

#Se obtendrá una lista con los precios
prices = list(map(lambda item: item['price'], items))
print(prices)

#Ahora se aplicará la función map para obtener el IVA de cada producto
#Primero, se crea una función que recibe un ítem y que devuelve el item con el IVA agregado
def add_iva(item):
    #Debemos partir haciendo una copia. De lo contrario, se modificará el diccionario original
    new_item = item.copy()
    new_item['iva'] = new_item['price'] *.19
    return new_item

#Ahora se utilizará la función map para agregar el iva a cada item de la lista items
new_items = list(map(add_iva, items))
print(new_items)

#El scope es el alcance que tiene una variable.
price = 100 #Variable global, definida en la línea de código principal. Puede ser usada dentro de una función tb.

def increment():
    p = price + 10 #p es una variable local. Sólo puede ser usada dentro de la función.
    return p

price_2 = increment()
print(price_2)

#Versión 2. Cuando la variable global se llama igual que la local, Python las reconoce como dos variables
#distintas y arroja error.

price_3 = 100
def increment_2():
    price_3 = price_3 + 10 #Error en esta línea de código.
    return price_3

price_4 = increment_2()
print(price_4)


#Higher order function es escribir una función dentro de otra función, ya sea como parámetro de entrada 
#o como return

def duplicate(x):
    return 2*x

def higher_order_function(x, function):
    return x + function(x)

result = higher_order_function(5, duplicate)
print(result)

#Haremos lo mismo con una función lambda
duplicate02 = lambda x : 2*x

higher_order_function02 = lambda x, function : x + function(x)

result2 = higher_order_function02(5, duplicate02)
print(result2)
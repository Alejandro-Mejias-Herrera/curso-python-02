#Crearemos una función que sumará los números enteros que se encuentren en un rango. 
#Retornará la suma.

print('La siguiente función sumará todos los números enteros en el rango indicado')

def sum_with_range(min, max):
    sum = 0
    for i in range (min,max+1):
        sum += i
    return sum

min = int(input('Ingrese el valor mínimo: '))
max = int(input('Ingrese el valor máximmo: '))
result = sum_with_range(min, max)
print(result)


#Se creará una función calculadora
input('La siguiente función realiza las cuatro operaciones matemáticas básicas entre dos números reales')

def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else: print('Error al ingresar los datos')
    return(result)

num1 = float(input('Ingrese el primer número: '))
op = input('Ingrese la operación que desea realizar. "+", "-", "*" o "/": ')
num2 = float(input('Ingrese el segundo número: '))

result = calculator(num1, op, num2)
print(result)


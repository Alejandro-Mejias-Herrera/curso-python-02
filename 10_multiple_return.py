#Crearemos una función que retorne dos valores, el área y perímetro de un cilindro
import math

def cylinder_area_volume(r,h):
    area = 2*math.pi*r*(r+h)
    vol = math.pi*r**2

    return area, vol

area, volume = cylinder_area_volume(3,5) 
print('Área: ',area,'Volumen: ', volume)

#Idea ampliación. Pedir al usuario que seleccione una figura geométrica en 3D y luego preguntar por los datos
#para calcular área y volumen.


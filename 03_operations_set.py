set_a = {'Chile', 'Argentina','Uruguay'}
set_b = {'Perú','Bolivia','Chile'}

#Unión de conjuntos. Elementos que están en set_a y en set_b.
set_c = set_a.union(set_b)
print(set_c)

set_d = set_a | set_b
print(set_d)

#Intersección de conjuntos. Elementos que están en ambos conjuntos.
set_c = set_a.intersection(set_b)
print(set_c)

set_d = set_a & set_b
print(set_d)

#Diferencia. Elementos que están en set_a, pero no están en set_b
set_c = set_a.difference(set_b)
print(set_c)

set_d = set_a - set_b
print(set_d)

#Diferencia simétrica. Elementos que están en set_a o en set_b, pero no en ambos.
set_c = set_a.symmetric_difference(set_b)
print(set_c)

set_d = set_a ^ set_b
print(set_d)
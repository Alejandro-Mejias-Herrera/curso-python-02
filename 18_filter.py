#Filter selecciona a los elementos que cumplen una condición en específico
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Usamos filter con una función lambda. Seleccionaremos a los números pares
#sintaxis: filter(función, iterable)
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(numbers)
print(new_numbers)


#FILTER CON DICCIONARIOS

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new_list = list(filter(lambda item : item['home_team_result'] == 'Win', matches))

print(matches)
print(len(matches))
print(new_list)
print(len(new_list))

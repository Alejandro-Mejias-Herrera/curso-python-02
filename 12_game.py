#Juego piedra papel y tijeras utilizando funciones
import random
#Se crea las variables globales para guardar el puntaje del usuario y de la máquina.
user_points = 0
computer_points = 0

#Función que transforma a número la elección del jugador y de la máquina.
def change_to_a_number(election):
    if election.lower() == 'piedra': return 0
    elif election.lower() == 'papel': return 1
    elif election.lower() == 'tijeras': return 2
    else: return 0

#Función que recibe las elecciones y los puntos. 
#Entrega un mensaje según se haya ganado o perdido y alcualiza los puntajes de usuario y máquina, retornándolos.
def result(user_choice, computer_choice,user_points,computer_points):
    if change_to_a_number(user_choice) - change_to_a_number(computer_choice) == 0:
        print(f'Empate. La máquina escogió {computer_choice}.\n Puntos jugador: {user_points}.\n Puntos máquina: {computer_points}.')
    elif change_to_a_number(user_choice) - change_to_a_number(computer_choice) in {1, -2}:
        user_points += 1
        print(f'Ganaste. La máquina escogió {computer_choice}.\n Puntos jugador: {user_points}.\n Puntos máquina: {computer_points}.')
    elif change_to_a_number(user_choice) - change_to_a_number(computer_choice) in {-1, 2}:
        computer_points += 1
        print(f'Perdiste. La máquina escogió {computer_choice}.\n Puntos jugador: {user_points}.\n Puntos máquina: {computer_points}.')
    else: print('Tu elección no es válida')

    return user_points, computer_points

#Función que arroja un mensaje en función del resultado final.
def final_result(user_points, computer_points):
    if user_points == 3:
        print('FELICIDADES. HAS GANADO EL JUEGO')
    else: print('LO SIENTO. HAS PERDIDO EL JUEGO')

#Mientras ningún puntaje llegue a 3, se continúa jugando.
while user_points < 3 and computer_points < 3:
    user_choice = input('ingresa piedra, papel o tijeras\n')
    computer_choice = random.choice(['piedra','papel','tijeras'])
    user_points, computer_points = result(user_choice, computer_choice, user_points, computer_points)

#Cuando algún puntaje llega a 3, se muestra el puntaje final.
final_result(user_points, computer_points)


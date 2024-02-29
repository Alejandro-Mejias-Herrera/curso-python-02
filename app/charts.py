#Se importa la libraría. Como el nombre es complicado, se debe hacer con un alias
#matplotlib no es una librería que viene con python, sino que la hizo la comunidad. Se debe instalar
#En la terminal, se debe secribir pip install matplotlib
import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
    #fig y las coordenadas de la gráfica
    fig, ax = plt.subplots()
    #Gráfica de barras
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [60, 90, 40]
    #generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)

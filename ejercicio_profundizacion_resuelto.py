'''
SQL Introducción [Python]
Ejercicio de Profundización
---------------------------
Autor: Inove Coding School
Resuelto por: Valentín Imperio

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''
# Importo las librerias a utilizar

import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
# Visualizador de bases de datos .db:
# https://extendsclass.com/sqlite-browser.html


def fetch():
    # Deben crear una función "fetch" que lea el valor de la columna "pulso" 
    # de todas las filas de la tabla "sensor" de la base de datos "heart.db".\
    # Deben usar la sentencia SELECT indicando que desean leer solamente la columna pulso,
    # y leer todo junto utilizando "fetchall".\
    # Al finalizar la función rebe retornar la lista de todos los pulsos cardícos obtenidos de la tabla.
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    
    # Conexión a la base de datos.
    conn = sqlite3.connect('heart.db') 
    # Creación del cursor.
    c = conn.cursor()

    # Ejecutar query. Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM sensor')
    
    print('Recorrer los datos desde el cursor y obtener todos los datos juntos.')
    data = c.fetchall() # Para guardar toda la info que está guardada en el cursor.
                        # Es decir se le pide toda la INFO al cursor y se la guarda en una variable.

    # Cerrar la conexión con la base de datos.
    conn.close()

    return data


def show(data):
    print("A continuación se muestra el gráfico de las pulsaciones vs tiempo.")

    tiempo = [x[0] for x in data]
    pulsaciones = [y[1] for y in data]

    fig = plt.figure() 
    ax = fig.add_subplot()
    ax.bar(tiempo,pulsaciones, color="tab:purple")
    ax.set_title("Ritmo Cardíaco")
    ax.set_ylabel(" Pulsaciones ")
    ax.set_xlabel(" Tiempo ")    
    plt.show() 


def estadistica(data):
    pulsaciones = [y[1] for y in data]

    mean = np.mean(pulsaciones)
    std = np.std(pulsaciones)
    max = np.amax(pulsaciones)
    min = np.amin(pulsaciones)

    print("El valor mínimo es: ")
    print(min)
    print("El valor máximo es: ")
    print(max)
    print("El valor medio es: ")
    print(mean)
    print("El desvío estandar es:")
    print(std)
    

def regiones(data):
    pulsaciones = [y[1] for y in data]

    mean = np.mean(pulsaciones)
    std = np.std(pulsaciones)

    # Inicialización de las variables lista.
    x1 = []
    y1 = []
    
    x2 = []
    y2 = []

    x3 = []
    y3 = []
    
    # Se llenan las listas:
    for i in range(len(pulsaciones)):
        if pulsaciones[i] <= (mean-std):
            x1.append(i)
            y1.append(pulsaciones[i])

        elif pulsaciones[i] >= (mean+std):
            x2.append(i)
            y2.append(pulsaciones[i])
        else:
            x3.append(i)
            y3.append(pulsaciones[i])

    # Una vez obtenidos las listas mencionadas, debe dibujar tres scatter plot en un solo 
    # gráfico. Cada uno de los tres scatter plot representa cada una de las listas
    # mencionadas que debe dibujar con un color diferente.

    print("Se muestra el gráfico con sus respectivas regiones: ")
    fig = plt.figure()
    fig.suptitle("Pulsaciones al ver un partido de fútbol", fontsize = 16, weight = "bold")
    ax  = fig.add_subplot()
    ax.scatter(x1, y1, label='Aburrimiento', color = "b", s=2)
    ax.scatter(x2, y2, label='Entusiasmo', color = "r", s=2)
    ax.scatter(x3, y3, label='Tranquilidad', color = "g", s=2)
    ax.set_facecolor("whitesmoke")
    ax.grid("solid")
    ax.legend()
    ax.set_xlabel("Id")
    ax.set_ylabel("Pulsaciones")
    plt.show()


if __name__ == "__main__":
    
    # Seteo directorio
    os.getcwd()
    os.chdir(os.path.dirname(__file__))
    
    # Leer la DB
    data = fetch()

    # Data analytics
    show(data)
    estadistica(data)
    regiones(data)
# creo el main
from funciones import *


def elegir():
    variable = int(input("\nEjercicios de Archivos en Python. \n\nPor favor, introduzca qué ejercicio desea realizar: \n --> 1: Información de los exámenes y la asistencia de cada alumno \n --> 2: nota final del curso \n --> 3: Alumnos aprobados y suspensos\n"))
    if variable == 1:
        from funciones import funcion1
    elif variable == 2:
        from funciones import funcion2
    elif variable == 3:
        from funciones import funcion3
    else:
        print("Sólo son válidos los valores 1,2 y 3.\n")
elegir()

import csv

def funcion1(calificaciones):
    calificaciones = []
    with open(funcion1, 'r') as f:
        for linea in f:
            funcion1.append(linea.split())
    return funcion1


# función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

# Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas


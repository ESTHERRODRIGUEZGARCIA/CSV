# Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios con las calificaciones de cada alumno.

def calificaciones(fichero):
    calificaciones = []
    with open(fichero, 'r') as f:
        for linea in f:
            calificaciones.append(linea.split())
    return calificaciones


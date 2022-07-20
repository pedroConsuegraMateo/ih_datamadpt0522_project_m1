import pandas as pd
import math
from modules import geo_calculations as gc

# Obtención de coordenadas de centros

def start_points(centros):
    
    start_points = []
    for centro in range(len(centros)):

        start_point = (float(centros['location.latitude'][centro]), float(centros['location.longitude'][centro]))
        start_points.append(start_point)
    
    return start_points


# Obtención de coordenadas de paradas

def finish_points(bicimad):
    
    finish_points = []
    for parada in range(len(bicimad)):
        
        lat_long = bicimad['geometry.coordinates'][parada].split(', ')
        lat = lat_long[0][1:]
        long = lat_long[1][:-1]
        finish_point = (float(lat),float(long))
        finish_points.append(finish_point)

    return finish_points

# Función de distancias mínimas

def min_distance(start_point, finish_points):
    
    parada = 0
    min_distance = float(math.inf)
    index_distance = (-1,-1)
    for j in finish_points:
        
        distance = gc.distance_meters(start_point[0], start_point[1],j[1],j[0])
        if distance.iloc[0] < min_distance:
            min_distance = distance.iloc[0]
            index_distance = (parada, min_distance)
        parada+=1
        
    return index_distance


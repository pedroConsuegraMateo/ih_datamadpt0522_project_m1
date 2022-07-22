import pandas as pd

# Creación de la tabla principal junto a las coordenadas


def main_table_with_extras(centros, bicimad, distancias, start_points, finish_points):
    
    centros[['title','address.street-address']]
    centros['parada'] = ''
    centros['dirección parada'] = ''
    centros ['distancia (m)'] = ''
    centros['latitud_centro'] = ''
    centros['longitud_centro'] = ''
    centros['latitud_parada'] = ''
    centros['longitud_parada'] = ''
    
    for i in range(len(centros)):
        centros['parada'].loc[i] = bicimad['name'].loc[distancias[i][0]]
        centros['dirección parada'].loc[i] = bicimad['address'].loc[distancias[i][0]]
        centros ['distancia (m)'].loc[i] = distancias[i][1]
        
        centros['latitud_centro'].loc[i] = start_points[i][0]
        centros['longitud_centro'].loc[i] = start_points[i][1]
        centros['latitud_parada'].loc[i] =  finish_points[distancias[i][0]][1]
        centros['longitud_parada'].loc[i] = finish_points[distancias[i][0]][0]

    main_table_extra = centros[['title','address.street-address','parada','dirección parada', 'distancia (m)', 'latitud_centro', 'longitud_centro', 'latitud_parada', 'longitud_parada']]
    #main_table_extra = main_table_extra.rename({'title': 'Place of Interest', 'address.street-address':'Place Address', 'parada':'BiciMAD Station', 'dirección parada':'Station Location', 'distancia (m)':'distance (m)'}, axis=1)
    
    
    return main_table_extra

# Creación de la tabla principal

def main_table(main_table_extra):

    main_table = main_table_extra[['title','address.street-address','parada','dirección parada']]
    main_table = main_table_extra.rename({'title': 'Place of Interest', 'address.street-address':'Place Address', 'parada':'BiciMAD Station', 'dirección parada':'Station Location'}, axis=1)
    
    
    return main_table[['Place of Interest', 'Place Address', 'BiciMAD Station', 'Station Location']]
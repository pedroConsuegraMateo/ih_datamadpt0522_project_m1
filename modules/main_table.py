import pandas as pd

# Creación de la tabla principal

def main_table(centros, bicimad, distancias):
    
    centros[['title','address.street-address']]
    centros['parada'] = ''
    centros['dirección parada'] = ''
    centros ['distancia (m)'] = ''
    
    for i in range(len(centros)):
        centros['parada'].loc[i] = bicimad['name'].loc[distancias[i][0]]
        centros['dirección parada'].loc[i] = bicimad['address'].loc[distancias[i][0]]
        centros ['distancia (m)'].loc[i] = distancias[i][1]

    main_table = centros[['title','address.street-address','parada','dirección parada', 'distancia (m)']]
    main_table = main_table.rename({'title': 'Place of Interest', 'address.street-address':'Place Address', 'parada':'BiciMAD Station', 'dirección parada':'Station Location', 'distancia (m)':'distance (m)'}, axis=1)
    
    
    return main_table
from modules import connections as c
from modules import geo_calculations as gc
from modules import points_and_distances as pad
from modules import main_table as mt

import argparse
from fuzzywuzzy import process

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Obtención de las paradas más cercanas a cada centro médico' )
    help_message ='Elige una opción. Option 1: "all" devuelve una tabla con todos los datos centro-parada. Option 2: "NOMBRE_CENTRO" devuelve el registro centro-parada indicado' 
    parser.add_argument('-f', '--function', help=help_message, type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    
    centros = c.centros_atencion_medica()
    bicimad = c.bicimad_connection()
    
    start_points = pad.start_points(centros)
    finish_points = pad.finish_points(bicimad)
    distancias = [pad.min_distance(i,finish_points) for i in start_points]
    
    main_table = mt.main_table(centros, bicimad, distancias)
    
    
    if argument_parser().function == 'all':
        main_table.to_csv('./data/main_table.csv')
    else:
        nombre = argument_parser().function
        
        aproximacion = ''
        precision = -1
        for i in range(len(main_table)):
            if precision < process.extractOne(str(nombre), main_table['Place of Interest'][i])[1]:
                aproximacion = process.extractOne(str(nombre), main_table['Place of Interest'][i])[0]
                precision = process.extractOne(str(nombre), main_table['Place of Interest'][i])[1]
                 
        
        main_table = main_table[main_table['Place of Interest'] == aproximacion]
        aproximacion = aproximacion.replace(' ', '_')
        main_table.to_csv(f'./data/{aproximacion}.csv')
        
    print('Finish!! :)')
    
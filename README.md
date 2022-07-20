# Proyecto Módulo 1

El objetivo de este proyecto es la creación de una tabla que nos devuelva la estación de BiciMAD más cercana a cada Centro Médico de la Comunidad de Madrid; o bien la estación BiciMAD más cercana a un centro médico que introduzca el usuario. 


## Librerías Usadas

- sqlalchemy - Para el acceso a la base de datos de BiciMAD
- requests - Para el acceso a los datos de los centros de atención médica del ayuntamiento de Madrid
- pandas
- argparse
- geopandas & shapely.geometry - Para el cálculo de distancias
- fuzzywuzzy - Para mejorar y facilitar la experiencia del usuario
- folium - Para generar mapas

## Módulos

El proyecto consta de 4 módulos y el script principal. Los 4 módulos son los siguientes:

### connections.py

Incluye las dos funciones necesarias para la recogida de datos. 

- bicimad_connection: conecta con la base de datos de bicimad, devuelve una tabla de 
- centros_atencion_medica: conecta con los datos de los centros de atención médica de Madrid. Devuelve una tabla de pandas

### geo_calculations.py

Incluye las dos funciones que calcularán las distancias reales entre dos puntos de coordenadas que reciban.

- to_mercator: recibe una coordenada de latitud y otra de longitud. Transforma el par latitud-longitud que recibe a un par  equivalente en un plano. Es utilizada por la función distance_meters
- distance_meters: recibe dos pares de coordenadas(4 floats). Calcula la distancia entre dos pares de coordenadas que recibe. Devuelve un float.

### points_and_distances.py

Incluye las funciones necesarias para obtener la distancia entre un centro y la parada más cercana a ese centro.

- start_points: recibe el dataframe de los centros. Devuelve un list de tuplas. Cada tupla es un par de coordenadas que representa cada centro médico.
- finish_points: recibe el dataframe de las paradas de BiciMAD. Devuleve un list de tuplas donde cada tupla es un par de coordenadas que representa cada parada.
- min_distance: recibe un start_point y el list con todos los finish_points. Calcula el par de coordenadas cuya distancia al start_point que recibe es la menor. Devuelve una tupla formada por ese par de distancia óptima y la distancia calculada.

### main_table.py

Consta de dos funciones que se encargan de crear la tabla principal y otra con 5 columnas más que corresponden a las coordenadas de cada parada y cada centro; y las distancias entre ellos.

- main_table_with_extras: recibe el dataframe de los centros, una lista con sus coordenadas, un dataframe de las paradas, una lista con sus coordenadas y las distancias.
- main_table: recibe la tabla con los extras. Devuelve un dataframe con las columnas pedidas.


## Pain Points:

- velocidad de cálculo de distancias. primer método fallido.
- problema para crear mapas con la lista de coordenadas de las paradas. Puede resultar confusa la solución.
 
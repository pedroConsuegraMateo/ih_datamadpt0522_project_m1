import folium
import pandas

def map_generator(main_table_extras):
    
    
    map = folium.Map(location=[40.416948896201355, -3.7038645330446434], zoom_start=12)
    folium.Marker(location=[main_table_extras['latitud_parada'] , main_table_extras['longitud_parada']],
                  popup=main_table_extras['parada'],
                  icon=folium.Icon(icon="bicycle", prefix='fa', color='red')).add_to(map)
    
    folium.Marker(location=[main_table_extras['latitud_centro'], main_table_extras['longitud_centro']],
                  popup=main_table_extras['title'],
                  icon=folium.Icon(icon="home", prefix='fa', color='blue')).add_to(map)
    
    map.save('place.html')
    
    return True
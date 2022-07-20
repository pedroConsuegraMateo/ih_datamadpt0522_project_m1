import folium
import pandas

def map_generator(centro_parada):
    
    print(centro_parada['latitud_parada'])
    print(centro_parada['longitud_parada'])
    print(centro_parada['latitud_centro'])
    print(centro_parada['longitud_centro'])
    
    map = folium.Map(location=[40.416948896201355, -3.7038645330446434], zoom_start=12)
    folium.Marker(location=[centro_parada['latitud_parada'], centro_parada['longitud_parada']],
                  popup=centro_parada['parada'],
                  icon=folium.Icon(icon="bicycle", prefix='fa', color='red')).add_to(map)
    
    folium.Marker(location=[centro_parada['latitud_centro'], centro_parada['longitud_centro']],
                  popup=centro_parada['title'],
                  icon=folium.Icon(icon="home", prefix='fa', color='blue')).add_to(map)
    
    map.save('place.html')
    
    return True
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import inspect
import requests
import pandas as pd

# Conexión a BiciMAD

def bicimad_connection():
    
    engine = create_engine('mysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD')
    inspector = inspect(engine)
    inspector.get_table_names()
    
    bicimad = pd.read_sql_query("SELECT * FROM bicimad_stations", engine)
    
    return bicimad

# Conexión a centros médicos de Madrid

def centros_atencion_medica():
    
    response = requests.get('https://datos.madrid.es/egob/catalogo/212769-0-atencion-medica.json')
    json = response.json()
    
    centros = pd.DataFrame(pd.json_normalize(json['@graph']))
    
    return centros
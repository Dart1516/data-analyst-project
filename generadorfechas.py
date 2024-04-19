import pandas as pd
import random
from datetime import datetime, timedelta

# Función para generar fechas aleatorias dentro de un rango
def generar_fecha():
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    fecha_aleatoria = start_date + timedelta(days=random_days)
    return fecha_aleatoria

# Carga el archivo Excel en un DataFrame de Pandas
df = pd.read_excel('prueba.xlsx')

# Convierte la columna de fechas al tipo de dato adecuado (datetime64[ns])
df['data'] = pd.to_datetime(df['data'])

# Genera fechas aleatorias para las filas vacías
filas_vacias = df[df['data'].isnull()].index
for idx in filas_vacias:
    df.at[idx, 'data'] = generar_fecha()

# Formatea la columna 'data' en el formato deseado (dd-mm-yyyy)
df['data'] = df['data'].dt.strftime('%d-%m-%Y')

# Guarda el DataFrame modificado en un nuevo archivo Excel
df.to_excel('prueba2.xlsx', index=False)
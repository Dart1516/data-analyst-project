import pandas as pd
import random
from datetime import  datetime, timedelta


# Carga el archivo Excel en un DataFrame de Pandas
df = pd.read_excel('denuncias.xlsx')
# Agrupa por nombre de empresa y cuenta las denuncias
df['quantidade'] = df.groupby('nome')['denuncia'].transform('count')
# Guarda el DataFrame modificado en un nuevo archivo Excel
df.to_excel('prueba.xlsx', index=False)


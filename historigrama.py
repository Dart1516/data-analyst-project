import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
df = pd.read_excel('datos_anonimos.xlsx')

# Convertir la columna 'data' al tipo de dato adecuado (datetime) y especificar el formato
df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y')

# Agrupar las denuncias por semana y contar la cantidad de denuncias por semana
denuncias_por_semana = df.groupby(df['data'].dt.isocalendar().week)['quantidade'].sum()

# Crear el gráfico de línea
plt.plot(denuncias_por_semana.index, denuncias_por_semana, color='skyblue', marker='o')

# Personalizar el gráfico
plt.title('Cantidad de Denuncias por Semana')
plt.xlabel('Semana del Año (ISO)')
plt.ylabel('Cantidad de Denuncias')
plt.grid(True)

# Mostrar el gráfico
plt.show()

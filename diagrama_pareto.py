import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
df = pd.read_excel('datos_anonimos.xlsx')

# Convertir la columna 'data' al tipo de dato adecuado (datetime) y especificar el formato
df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y')

# Agrupar las denuncias por semana y contar la cantidad de denuncias por semana
denuncias_por_semana = df.groupby(df['data'].dt.isocalendar().week)['quantidade'].sum()

# Calcular la frecuencia acumulada
frecuencia_acumulada = denuncias_por_semana.cumsum()

# Crear el gráfico
fig, ax1 = plt.subplots()

# Gráfico de barras para las denuncias por semana
ax1.bar(denuncias_por_semana.index, denuncias_por_semana, color='skyblue', edgecolor='black')
ax1.set_xlabel('Semana del Año (ISO)')
ax1.set_ylabel('Cantidad de Denuncias', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Segundo eje y para la línea de frecuencia acumulada
ax2 = ax1.twinx()
ax2.plot(frecuencia_acumulada.index, frecuencia_acumulada, color='red', marker='o')
ax2.set_ylabel('Frecuencia Acumulada', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Personalizar el gráfico
plt.title('Diagrama de Pareto: Denuncias por Semana y Frecuencia Acumulada')
plt.grid(True)

# Mostrar el gráfico
plt.show()

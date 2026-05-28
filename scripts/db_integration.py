import sqlite3
import pandas as pd

# Cargar el dataframe (desde donde lo guardaste)
df = pd.read_csv('../datos/procesado/clientes_con_clusters.csv')

# Conectar a la base de datos
conn = sqlite3.connect('../base_datos/clientes_segmentados.db')

# Guardar la tabla en SQLite
df.to_sql('clientes', conn, if_exists='replace', index=False)

print("Base de datos creada exitosamente")

# Consultas de ejemplo
print("\n=== Promedio de Valor de Pedido por Cluster ===")
query1 = "SELECT Cluster, AVG(Average_Order_Value) as promedio_valor FROM clientes GROUP BY Cluster"
print(pd.read_sql(query1, conn))

print("\n=== Conteo de clientes por Cluster ===")
query2 = "SELECT Cluster, COUNT(*) as cantidad FROM clientes GROUP BY Cluster"
print(pd.read_sql(query2, conn))

# Cerrar conexión
conn.close()
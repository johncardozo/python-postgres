import psycopg2
from datos_conexion import dc

# Conexión a la base de datos
conexion = psycopg2.connect(**dc)

# Creación de cursor
cursor = conexion.cursor()

# Ejecución de la sentencia
cursor.execute('select * from empleados')

# Obtiene los registros
registros = cursor.fetchall()

# Recorre los registros
for registro in registros:
    # Obtiene las columnas id (0) y nombres (1)
    id = registro[0]
    nombres = registro[1]
    # Imprime los datos
    print(f'id={id}\tnombres={nombres}')

# Cerrar el cursor
cursor.close()

# Cerrar la conexión
conexion.close()

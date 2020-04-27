import psycopg2
from datos_conexion import dc

# Conexión a la base de datos
conexion = psycopg2.connect(**dc)

# Creación de cursor
cursor = conexion.cursor()

# Cadena SQL
sql = 'delete from empleados where id=%s'

# Parametros de la cadena
parametros = ('3')

# Ejecución de la sentencia
cursor.execute(sql, parametros)

# Elimina los datos en la base de datos
conexion.commit()

# Cerrar el cursor
cursor.close()

# Cerrar la conexión
conexion.close()

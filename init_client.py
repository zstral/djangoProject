#Este script sirve para forzar el inicio de Instant Client de Oracle
#en caso de que haya problemas con las variables de entorno de windows
#o Django no detecte el path adecuado.

#Debes configurar la ruta manualmente para que funcione C:\Users\tunombredeusuario\...

import oracledb

try:
    oracledb.init_oracle_client(lib_dir=r"C:\Users\tunombredeusuario\...")
except oracledb.Error as e:
    print(f"Error al inicializar Instant Client: {e}")
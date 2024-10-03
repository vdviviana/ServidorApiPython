# Contiene la configuración de la base de datos
import os
#
from flask import Flask
from flask import request #para metodo POST
from flaskext.mysql import MySQL

from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicializa nombre de mi aplicación con la aplicación Flask
app = Flask(__name__)
# Inicializa variable de tipo mysql
mysql = MySQL()

# Configuración de la base de datos usando variables de entorno
app.config['MYSQL_DATABASE_HOST']= os.getenv('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_USER']=os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD']=os.getenv('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB']=os.getenv('MYSQL_DATABASE_DB')

# inicializar la database con la aplicacion Flask
mysql.init_app(app)

def test_connection():
    conn =mysql.connect()
    cursor = conn.cursor()
    #conn = psycopg2.connect(**DATABASE_CONFIG)
    #conn =mysql.connect(**DATABASE_CONFIG)
    #cursor = conn.cursor()
    #cur = conn.cursor()
    conn.commit()
    cursor.close()
    conn.close()

    print("* * TEST CONECTION - OK * *")
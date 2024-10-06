#define los modelos de datos que se implementaran en la aplicación
from app.database import get_db


# cuando construya un nuevo objeto Users pedira todos estos datos
class Users:
    def __init__(self,id=None,nombre=None, correo=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    #--- serialización para conversión a jsonify (si fuera necesario)
    def serialize(self):
        return {'id': self.id,
        'nombre': self.nombre,
        'correo': self.correo
        }

    #--- funcion ejecuta cualquier query que le pase como parametro
    @staticmethod
    def __get_users_by_query(query):
        db= get_db() # conecto a db (funcion viene de database.py)
        cursor= db.cursor()
        cursor.execute(query)
        rows= cursor.fetchall() # me devuelve todo y guardo resultados en lista

        users= [] # creo array
        for row in rows: # recorro lista y voy almacenando cada fila y posicion
            users.append(
                Users( id=row[0], nombre=row[1], correo=row[2])
            )
        cursor.close()
        return users

    #------------------

    #--- consulta trae todos los usuarios
    @staticmethod
    def get_users_all():
        return Users.__get_users_by_query("SELECT * FROM usuarios")

    #------------------

    #--- consulta usuarios por id
    @staticmethod
    def get_by_id(id):
        db = get_db() # conecto a db (funcion viene de database.py)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id))
        row = cursor.fetchone() # me devuelve un dato y guardo resultado en variable
        cursor.close()
        if row: # si el usuario existe, devuelvo el usuario
            return Users( id=row[0], nombre=row[1],correo=row[2] )
        return None # si ek usuario no existe, no devuelvo nada

    #------------------

    #--- update / insert
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id: # Actualizar usuario existente
            cursor.execute("UPDATE usuarios SET nombre = %s, correo = %s WHERE id = %s", (self.nombre, self.correo))
        else: # Crear usuario nuevo
            cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (self.nombre, self.correo))
            self.id= cursor.lastrowid
        db.commit()
        cursor.close()

    #------------------











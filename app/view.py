#define las rutas y la logica de negocio de la aplicacion

# jsonify define json a partir de objetos python
from flask import jsonify,request
from app.model import Users

# -------------- test de conexión a la base de datos ----------------
# ----
# 
def index():

    #devuelve json de datos como api
    return jsonify({
        'mensaje': 'Hello World APIS con FLASK'})
    #las llaves hablan de diccionario

# -------------- recibe peticion request, toma datos recibidos  ----------------
# ---- crea nuevo users
# 
def create_new_user():
 #datos recibidos en formato json
    data = request.json
    new_user = Users(
        nombre=data['nombre'],
        correo=data['correo']
        )
    new_user.save()
    return jsonify({'message': 'User created successfully'}), 201

# ---- trae todos los usuarios
# 
def get_view_users_all(): 
    users = Users.get_users_all()
    return jsonify([user.serialize() for user in users])


# ---- recibe id devuelve usuarios por id
# 
def get_users_byid(users_id):
    user = Users.get_by_id(users_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.serialize())
# --------------  
# ----
# 

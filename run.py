from flask import Flask
from app.view import *
from app.database import *
from flask_cors import CORS

# primero identifico 'app' como nuevo objeto Flask
app =Flask(__name__)

# -------------- rutas  ----------------
# ---- 
# 

# rutas de mi Api REst
app.route('/', methods =[ 'GET'])(index)

# ruta de funcion de la vista -> crea usuario mediante post
app.route('/api/users/create/', methods=['POST'])(create_new_user)

# ruta funcion de la vista -> consulta usuarios
app.route('/api/users/all/', methods=['GET'])(get_view_users_all)

# ruta de funcion de la vista -> consulta user por id
app.route('/api/users/byid/<int:users_id>', methods=['GET'])(get_users_byid)

# --------------  
# ----
# 

# llamo function de modelo
#test_connection()

init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)

if __name__== '__main__':
	app.run(debug=True)

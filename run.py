from flask import Flask
from app.view import *
from app.database import test_connection

# primero identifico 'app' como nuevo objeto Flask
app =Flask(__name__)

# rutas de mi Api REst
app.route('/', methods =[ 'GET'])(index)

# llamo function de modelo
test_connection()

if __name__== '__main__':
	app.run(debug=True)

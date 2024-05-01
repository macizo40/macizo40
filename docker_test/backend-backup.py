import psycopg2
import json
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask_cors import CORS
#variable llamada conn para la base de datos
conn = psycopg2.connect(database="postgres",
                        host="127.0.0.1",
                        user="admin",
                        password="admin",
                        port=51347)

print("Si me pude conectar")
#Curso para ejecutar query en la base de datos
cursor = conn.cursor()

app = Flask(__name__)
cors = CORS(app)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/empleados')
# ‘/’ URL is bound with hello_world() function.
def get_empleados():
    cursor.execute("SELECT * FROM empleados;")
    empleados = cursor.fetchall()
    return json.dumps(empleados),200

@app.route('/empleados/<id>')  # /landingpage/A
def get_empleado(id):
    cursor.execute(f"SELECT name FROM empleados WHERE id={id}")
    empleado = cursor.fetchone()
    return json.dumps(empleado),200
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=8081)
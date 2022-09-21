
from flask import Flask as FL,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = FL(__name__)

mysql = MySQL(app)
CORS(app)
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_PORT'] = 3600
app.config['MYSQL_USER'] = "usuario"
app.config['MYSQL_PASSWORD'] = "12345"
app.config['MYSQL_DB'] = "actividad"
@app.get("/listar")
def listar():
    if request.method == 'GET':
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''SELECT * FROM usuario;''')
            personasd = cur.fetchall()

            personas_disponibles = []

            for persona in personasd:
                pers = {
                    'id_usuario': persona[0],
                    'nombre': persona[1],
                    'apellido': persona[2],
                    'direccion': persona[3],
                    'telefono': persona[4],
                    'correo': persona[5]
                }
                personas_disponibles.append(pers)
            return personas_disponibles, 200
        except Exception as error:
            print(error)
@app.post("/insertar")
def insertar():

    if request.method == 'POST':
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        telefono = request.json['telefono']
        correo = request.json['correo']
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''INSERT INTO usuario (nombre, apellido, direccion, telefono, correo) VALUES ('{nombre}', '{apellido}', '{direccion}', '{telefono}', '{correo}'); COMMIT;''')
            personasd = cur.fetchall()
            return { 'mensaje': 'Usuario insertado con éxito.' }, 200
        except Exception as error:
            print(error)
    pass
@app.delete("/borrar")
def borrar():
    if request.method == 'DELETE':
        id_usuario = request.json['id_usuario']
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''DELETE FROM usuario WHERE id_usuario = {id_usuario}; COMMIT;''')
            personasd = cur.fetchall()
            return { 'mensaje': 'Usuario Eliminado' }, 200
        except Exception as error:
            print(error)
    pass
@app.put("/editar")
def editar():
    if request.method == 'PUT':
        id_usuario = request.json['id_usuario']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        correo = request.json['correo']
        try:
            cur = mysql.connection.cursor()
            cur.execute(f'''UPDATE usuario SET nombre='{nombre}',  apellido='{apellido}',  direccion='{direccion}',  telefono='{telefono}',  correo='{correo}' WHERE id_usuario = {id_usuario}; COMMIT;
''')
            personasd = cur.fetchall()
            return { 'mensaje': 'Usuario editado' }, 200
        except Exception as error:
            print(error)
    
    pass
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)
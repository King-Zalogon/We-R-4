from flask import Flask, jsonify, request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/profesores'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino la tabla
class Profesor(db.Model):   # la clase Profesor hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    apellido=db.Column(db.String(100))
    nombre=db.Column(db.String(100))
    email=db.Column(db.String(100))
    telefono=db.Column(db.Integer)
    materia=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,apellido, nombre, email, telefono, materia, imagen):   #crea el  constructor de la clase
        self.apellido=apellido
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.email=email
        self.telefono=telefono
        self.materia=materia
        self.imagen=imagen


    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class ProfesorSchema(ma.Schema):
    class Meta:
        fields=('id','apellido', 'nombre', 'email', 'telefono', 'materia', 'imagen')




profesor_schema=ProfesorSchema()            # El objeto profesor_schema es para traer un Profesor
profesores_schema=ProfesorSchema(many=True)  # El objeto profesores_schema es para traer multiples registros de profesor




# crea los endpoint o rutas (json)
@app.route('/profesores',methods=['GET'])
def get_Profesores():
    all_profesores=Profesor.query.all()         # el metodo query.all() lo hereda de db.Model
    result=profesores_schema.dump(all_profesores)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/Profesores/<id>',methods=['GET'])
def get_Profesor(id):
    Profesor=Profesor.query.get(id)
    return profesor_schema.jsonify(Profesor)   # retorna el JSON de un Profesor recibido como parametro




@app.route('/Profesores/<id>',methods=['DELETE'])
def delete_Profesor(id):
    Profesor=Profesor.query.get(id)
    db.session.delete(Profesor)
    db.session.commit()
    return profesor_schema.jsonify(Profesor)   # me devuelve un json con el registro eliminado


@app.route('/Profesores', methods=['POST']) # crea ruta o endpoint
def create_Profesor():
    #print(request.json)  # request.json contiene el json que envio el cliente
    apellido=request.json['apellido']
    nombre=request.json['nombre']
    email=request.json['email']
    telefono=request.json['telefono']
    materia=request.json['materia']
    imagen=request.json['imagen']
    new_Profesor=Profesor(apellido, nombre, email, telefono, materia, imagen)
    db.session.add(new_Profesor)
    db.session.commit()
    return profesor_schema.jsonify(new_Profesor)


@app.route('/Profesores/<id>' ,methods=['PUT'])
def update_Profesor(id):
    Profesor=Profesor.query.get(id)
 
    apellido=request.json['apellido']
    nombre=request.json['nombre']
    email=request.json['email']
    telefono=request.json['telefono']
    materia=request.json['materia']
    imagen=request.json['imagen']

    Profesor.apellido=apellido
    Profesor.nombre=nombre
    Profesor.email=email
    Profesor.telefono=telefono
    Profesor.materia=materia
    Profesor.imagen=imagen


    db.session.commit()
    return profesor_schema.jsonify(Profesor)
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000

from flask import Flask, jsonify, request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/we_r_4'
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
    materia=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,apellido, nombre, email, materia,imagen):   #crea el  constructor de la clase
        self.apellido=apellido
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.email=email
        self.materia=materia
        self.imagen=imagen


    #  si hay que crear mas tablas , se hace aqui

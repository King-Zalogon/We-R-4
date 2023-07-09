import sqlite3
from flask import Flask,jsonify,request

from flask_cors import CORS

DATABASE = "we-r-4.db"

#-------------------------------------------------------------------------------------

def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
#------------------------------------------------------------------------------------

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesores (
            nombre VARCHAR(25) NOT NULL,
            apellido VARCHAR(25) NOT NULL,
            correoElectronico VARCHAR(30) NOT NULL,
            telefono INTEGER(14) NOT NULL,
            fechaNac VARCHAR(12) NOT NULL,
            provincia VARCHAR(30),
            descripcion VARCHAR(360) NOT NULL,
            materia VARCHAR(30), 
            modalidad VARCHAR(30),
            foto TEXT NOT NULL 
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
    
def crear_db():
    conn = sqlite3.connect(DATABASE)
    crear_tabla()
    conn.close()
    
    

crear_db()

#--------------------------------------------------------------------------------------

class Profesor:
    
    def __init__(self,nombre,apellido,email,telefono,nacimiento,provincia,descripcion,materia,modalidad,foto):
        self.id =  None
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.nacimiento = nacimiento
        self.provincia = provincia
        self.descripcion = descripcion
        self.materia = materia 
        self.modalidad = modalidad
        self.foto = foto
        
    def modificar(self,nueva_provincia,nueva_descripcion,nueva_materia,nueva_modalidad,nueva_foto):
        self.provincia = nueva_provincia
        self.descripcion = nueva_descripcion
        self.materia = nueva_materia
        self.foto = nueva_foto
        self.modalidad = nueva_modalidad
        
class Profesores:
    def __init__(self):
        self.lista = []
    
    def consultar_profe(self,email):
        conect = conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM profesores WHERE correoElectronico = ?",(email,))
        row = cursor.fetchone()
        if row:
            return row
        return False
    
    def agregar(self,nombre,apellido,email,telefono,nacimiento,provincia,descripcion,materia,modalidad,foto):
        conect = conectar()
        cursor = conect.cursor()
        profesor_existente = self.consultar_profe(email)
        if profesor_existente:
            return jsonify({"mensaje":"Este email ya se encuentra registrado"})
        
        nuevo_profesor = Profesor(nombre,apellido,email,telefono,nacimiento,provincia,descripcion,materia,modalidad,foto)
        cursor.execute("""INSERT INTO profesores VALUES (?,?,?,?,?,?,?,?,?,?)""",
                           (nombre,apellido,email,telefono,nacimiento,provincia,descripcion,materia,modalidad,foto))
        conect.commit()
        
        return jsonify({"mensaje":"El registro se ha completado con éxito"}),200
    
    def modificar_profe(self,email,nueva_provincia,nueva_descripcion,nueva_materia,nueva_modalidad,nueva_foto):
        conect = conectar()
        cursor = conect.cursor()
        profesor_existente = self.consultar_profe(email)
        
        if profesor_existente:
            profesor_existente.modificar(nueva_provincia,nueva_descripcion,nueva_materia,nueva_modalidad,nueva_foto)
            cursor.execute("UPDATE profesores SET provincia = ?, descripcion = ?, materia = ?, modalidad = ?, foto = ? WHERE email = ?",(nueva_provincia,nueva_descripcion,nueva_materia,nueva_modalidad,nueva_foto,email))
            conect.commit()
            return{"mensaje":"Perfil modificado correctamente"},200
        
        return {"mensaje":"no se ha podido modificar el perfil"},200
    
    def listar_profesores(self):
        conect = conectar()
        cursor = conect.cursor()
        cursor.execute("SELECT * FROM profesores")
        filas = cursor.fetchall()
        profesores = []
        
        for fila in filas:
            nombre,apellido,email,telefono,nacimiento,provincia,descripcion,materia,modalidad,foto = fila
            profesor = {"nombre":nombre,"apellido":apellido,"email":email,"telefono":telefono,"nacimiento":nacimiento,"provincia":provincia,"descripcion":descripcion,"materia":materia,"modalidad":modalidad,"foto":foto}
            profesores.append(profesor)
        
        return jsonify(profesores),200
    
    def eliminar_profesor(self,email):
        conect = conectar()
        cursor = conect.cursor()
        profe__existente = self.consultar_profe(email)
        if profe__existente:
            cursor.execute("""DELETE FROM profesores WHERE email = ?""",(email,))
            if cursor.rowcount > 0:
                conect.commit()
                return jsonify({'mensaje': 'Profesor eliminado correctamente.'}), 200
            
        return jsonify({"mensaje":"No se ha podido eliminar al profesor"})
            
#------------------------------------------------------------------------------------
    
app = Flask(__name__)

CORS(app)



profesores = Profesores()

@app.route("/profesores", methods = ["POST"])
def agregar_profesor():
    
    email = request.json.get("email")
    nombre = request.json.get("nombre")
    apellido = request.json.get("apelllido")
    telefono = request.json.get("telefono")
    nacimiento = request.json.get("nacimiento")
    provincia = request.json.get("provincia")
    descripcion = request.json.get("descripcion")
    materia = request.json.get("materia")
    modalidad = request.json.get("modalidad")
    foto = request.json.get("foto")
    
    return profesores.agregar(nombre,apellido,email,nacimiento,provincia,descripcion,materia,foto)
    
@app.route("/profesores", methods = ["GET"])

def mostrar_profesores():
    return profesores.listar_profesores()
    
@app.route("/profesor/<string:email>",methods = ["PUT"])
def editar_perfil(email):
    
    nueva_provincia = request.json.get("nueva_provincia")
    nueva_descripcion = request.json.get("nueva_descripcion")
    nueva_materia = request.json.get("nueva_materia")
    nueva_modalidad = request.json.get("nueva_modalidad")
    nueva_foto = request.json.get("nueva_foto")
    
    return profesores.modificar_profe(email,nueva_provincia,nueva_descripcion,nueva_materia,nueva_modalidad,nueva_foto)

@app.route("/profesor/<string:email>", methods = ["DELETE"])
def eliminar(email):
    return profesores.eliminar_profesor(email)

app.run()  
    
    
    
    
    
    



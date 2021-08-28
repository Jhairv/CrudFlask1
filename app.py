from flask import Flask, request
from flask.helpers import url_for
from flask.templating import render_template
import psycopg2
from werkzeug.utils import redirect

conexion = psycopg2.connect(host='localhost', user='postgres', password='1234', database='CRUD')

cursor = conexion.cursor()
 
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_usuario = request.form['id']
        nombre = request.form['nombre']
        cargo = request.form['cargo']
        telefono = request.form['telefono']
        edad = request.form['edad']
        direccion = request.form['direccion']
        sql = 'insert into Empleados values(%s,%s,%s,%s,%s,%s)'
        values = (id_usuario, nombre, cargo, telefono, edad, direccion)
        cursor.execute(sql, values)
        conexion.commit()
        return redirect('/')
    if request.method == 'GET':
        sql = 'select * from Empleados'
        cursor.execute(sql)
        empleados = cursor.fetchall()
        conexion.commit()
        return render_template('create.html', empleados = empleados)
    return render_template('create.html') 

@app.route('/destroy/<id>')
def destroy(id):
    cursor.execute('delete from Empleados where id=%s', (id))
    conexion.commit()
    return redirect('/')

@app.route('/edit/<id>')
def edit (id): 
    cursor.execute('select * from empleados where id=%s', (id))
    empleados = cursor.fetchall()
    conexion.commit()
    return render_template('edit.html', empleados = empleados)
@app.route('/update',methods=['POST'])
def update():
    cur= conexion.cursor()
    _nombre=request.form['nombre']
    _cargo=request.form['cargo']
    _telefono=request.form['telefono']
    _edad=request.form['edad']
    _id=request.form["id"]
    _direccion=request.form["direccion"]
    query="UPDATE  empleados SET nombre=%s,cargo=%s,telefono=%s,edad=%s, direccion=%s WHERE id=%s;"
    datos=(_nombre,_cargo,_telefono, _edad, _direccion,_id)
    #query="INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (1966617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer') "
    cur.execute(query,datos)
    conexion.commit() 
    return redirect('/')
#  @app.route('/update', methods = ['POST'])
#  def update():
#          id_usuario = request.form['id']
#          nombre = request.form['nombre']
#          cargo = request.form['cargo']
#          telefono = request.form['telefono']
#          edad = request.form['edad']
#          direccion = request.form['direccion']
#          sql = 'update empleados set nombre = %s, cargo=%s, edad=%s, direccion=%s, telefono=%s where id= %s'
#          values = (id_usuario, nombre, cargo, telefono, edad, direccion)
#          print(values)
#          cursor.execute(sql, values)
#          conexion.commit()
#          return redirect('/')

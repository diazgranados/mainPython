from distutils.log import debug
from re import template
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def inicio():
    return render_template("index.html")


#@app.get("/contactos")
#def ListarContactos():
#    return render_template("dos.html")

@app.get("/edad")
def edad():
    return render_template("edad.html",año=edad)

@app.get("/edad/<int:contactoId>")#el int es para que en el navegador a la hora de buscar solamente me revisa un entero
def editarContactos(contactoId):
    edad=2022-contactoId
    return render_template("editar.html",edad=contactoId)


app.run(debug=True)
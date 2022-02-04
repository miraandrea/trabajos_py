from flask import Flask, render_template, request

app= Flask(__name__)

listaUsuario=[]
listaContraseña=[]

@app.route("/")
def index():
    a="lista usuario"
    b="lista contraseña"
    return render_template("index.html", lista1=listaUsuario, lista2= listaContraseña, a1=a, b2=b)

@app.route("/agregar")
def agregar():
    return render_template("1.html")
@app.route("/agregar/post", methods=["POST"])
def agregarpost():

    nombre= request.form["nombre"]
    contraseña= request.form["contraseña"]

    listaUsuario.append(nombre)
    listaContraseña.append(contraseña)

    a="lista usuario"
    b="lista contraseña"
    
    return render_template("index.html", lista1=listaUsuario, lista2= listaContraseña, a1=a, b2=b)

@app.route("/inicio")
def inicio():
    return render_template("/2.html")
@app.route("/inicio/post", methods=["POST"])
def iniciopost():

    nombre= request.form["usuario"]
    contraseña= request.form["contraseña"]

    listaUsuario.index(nombre)
    listaContraseña.index(contraseña)
    inicio="inicio correctamente"
    return render_template("index.html",ini=inicio)

@app.route("/eliminar")
def eliminar():
    return render_template("3.html")
@app.route("/eliminar/post", methods=["POST"])
def eliminarpost():

    contraseña= request.form["contraseña"]
    nombre= request.form["usuario"]

    listaUsuario.index(nombre)
    listaContraseña.index(contraseña)

    eliminar= request.form["nombre"]

    if eliminar in listaUsuario:
        el= listaUsuario.index(eliminar)
        listaContraseña[el]
        listaUsuario.pop(el)
        listaContraseña.pop(el)
        se="se elimino "

        a="lista usuario"
        b="lista contraseña"

        return render_template("index.html", lista1=listaUsuario, lista2= listaContraseña, a1=a, b2=b, se1=se)

@app.route("/mostrar")
def mostrar():

    a="lista usuario"
    
    return render_template("index.html", lista1=listaUsuario, a1=a)

@app.route("/buscar")
def buscar():
    return render_template("4.html")
@app.route("/buscar/post", methods=["POST"])
def buscarpost():

    nombre= request.form["usuario"]
    
    index=0
    liste=len(listaUsuario)

    while index < liste:
        if listaUsuario[index] == nombre:
            return render_template("index.html", lista1=listaUsuario[index], lista2= listaContraseña[index])
        index=index+1

if __name__ == "__main__":
    app.run(debug=True,port=5000)
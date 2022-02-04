from flask import Flask, render_template, request

app= Flask(__name__)


listaMascota = []
listaPropetario = []
listaTelefono = []

@app.route("/")
def index():
    a="lista mascotas"
    b="lista propetario"
    c="lista telefono"
    return render_template("index.html", lista1=listaMascota, lista2= listaPropetario,lista3=listaTelefono, a1=a, b2=b,c3=c)

@app.route("/agregar")
def agregar():
    return render_template("1.html")
@app.route("/agregar/post", methods=["POST"])
def agregarpost():

    nombre= request.form["mascota"]
    nombrep= request.form["propetario"]

    if nombrep in listaPropetario:
        PRINT="no se puede permitir dos mascotas con el mismo propetario"
        return render_template("index.html",m=PRINT)
    else:
        telefono= request.form["telefono"]
        listaMascota.append(nombre)
        listaPropetario.append(nombrep)
        listaTelefono.append(telefono)
        PRINT1="se agrego correctamente"
        a="lista mascotas"
        b="lista propetario"
        c="lista telefono"
        return render_template("index.html",lista1=listaMascota, lista2= listaPropetario,lista3=listaTelefono, a1=a, b2=b,c3=c,n=PRINT1)

@app.route("/consultar")
def inicio():
    return render_template("/2.html")
@app.route("/consultar/post", methods=["POST"])
def consultarpost():

    nombre= request.form["mascota"]
    nombrep= request.form["propetario"]

    listaMascota.index(nombre)
    listaPropetario.index(nombrep)

    index=0
    lista= len(listaMascota)
    lista= len(listaPropetario)

    while index < lista:
        if listaMascota[index]==nombre:
            if listaPropetario[index]== nombrep:
                PRINT3 ="Su numero de telefono es: "+ listaTelefono[index]
                return render_template("index.html",m1=PRINT3)
            else:
                PRINT4="Ingreso un dato mal."
                return render_template("index.html",n1=PRINT4)
        index=index+1

@app.route("/eliminar")
def eliminar():
    return render_template("3.html")
@app.route("/eliminar/post", methods=["POST"])
def eliminarpost():

    nombre= request.form["propetario"]
    telefono= request.form["telefono"]

    listaTelefono.index(telefono)
    contador=0
    listados= len(listaPropetario and listaTelefono)

    while contador < listados:
        if listaPropetario[contador]== nombre:
            if listaTelefono[contador]== telefono:
                if nombre in listaPropetario:
                    eliminar = listaPropetario.index(nombre)
                    listaMascota[eliminar]
                    listaMascota.pop(eliminar)
                    listaPropetario.pop(eliminar)
                    listaTelefono.pop(eliminar)
                    PRINT5="Se elimino correctamente"
                    a="lista mascotas"
                    b="lista propetario"
                    c="lista telefono"
                    return render_template("index.html", m2=PRINT5,lista1=listaMascota, lista2= listaPropetario,lista3=listaTelefono, a1=a, b2=b,c3=c)
            else:
                PRINT4="Ingreso un dato mal."
                return render_template("index.html",n1=PRINT4)
        contador=contador+1   
@app.route("/mostrar")
def mostrar():

    PRINT6="Nombre de las mascotas"
    PRINT7="Nombre de los dueños"
    PRINT8="Numero de telefono"

    return render_template("index.html",m11=PRINT6, n11=PRINT7,m12=PRINT8, lista1=listaMascota, lista2= listaPropetario,lista3=listaTelefono)
if __name__ == "__main__":
    app.run(debug=True,port=5000)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def inde():
    return render_template("inde.html")

@app.route("/primero")
def primero():
    return render_template("primero.html")
@app.route("/primero/post", methods=["POST"])
def primeropost():
    
    numero1 = request.form["calificacion1"]
    numero2 = request.form["calificacion2"]
    numero3 = request.form["calificacion3"]
    numero4 = request.form["calificacion4"]

    suma = (int(numero1) + int(numero2) + int(numero3) + int(numero4))/4
    return render_template("primero.html", valor = suma ) 

 

if __name__=="__main__":
    app.run(debug=True,port=5000)

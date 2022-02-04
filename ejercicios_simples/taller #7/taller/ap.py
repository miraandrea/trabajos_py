from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/")
def inde():
    return render_template("inde.html")

@app.route("/primero")
def primero():
    return render_template("primero.html")
@app.route("/primero/post", methods =["POST"])
def primeropost():
    
    numero1 = request.form["calificacion1"]
    numero2 = request.form["calificacion2"]
    numero3 = request.form["calificacion3"]
    numero4 = request.form["calificacion4"]

    suma = (int(numero1) + int(numero2) + int(numero3) + int(numero4))/4
    return render_template("primero.html", valoroperacion=suma)
@app.route("/segundo")
def segundo():
    return render_template("segundo.html")   
@app.route("/segundo/post", methods = ["POST"])
def segundopost():

    edad = request.form["edad"]
    return render_template("segundo.html", valor= edad)
@app.route("/tercero")
def tercero():
    return render_template("tercero.html")
@app.route("/tercero/post", methods=["POST"])
def terceropost():
    horas = request.form["horas"]
    pago = int(horas)*16
    paGO = int(horas)-40*20
    return  render_template(valorhoras = horas)
    return  render_template(valorpago1 = pago)
    return  render_template(valorpago2 = paGO)


if __name__ == "__main__":
    app.run(debug=True,port=5000)

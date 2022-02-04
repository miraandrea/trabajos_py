from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/suma/post", methods=["POST"])
def sumapost():

    num1 = request.form["numero1"]
    num2 = request.form["numero2"]

    suma = int(num1) + int(num2)

    return render_template("index.html", valorSuma = suma)
@app.route("/division/post", methods=["POST"])
def divisionpost():

    n1 = request.form["numero1"]
    n2 = request.form["numero2"]

    division = int(n1) % int(n2)

    return render_template("index.html", valordivision = division)
@app.route("/resta/post", methods=["POST"])
def restapost():

    nu1 = request.form["numero1"]
    nu2 = request.form["numero2"]

    resta = int(nu1)- int(nu2)

    return render_template("index.html", valorresta = resta)
@app.route("/multiplicacion/post", methods= ["POST"])
def multiplicacion():

    nume1 = request.form["numero1"]
    nume2 = request.form["numero2"]

    multiplicacion = int(nume1)* int(nume2)

    return render_template("index.html", valormultiplicacion = multiplicacion)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
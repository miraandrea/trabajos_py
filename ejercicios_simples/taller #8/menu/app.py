from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/primero")
def primero():
    return render_template("primero.html")
@app.route("/primero/post", methods= ["POST"])
def primerpost():

    n1 = request.form[numero1]
    n2 = request.form[numero2]
    n3 = request.form[numero3]

    diferente = int(n1) != int(n2) and int(n2) != int(n3) and int(n3) != int(n1)

    if int(n1)>int(n2) and int(n1)>int(n3) and diferente:
        return int(n1) + "es mayor y diferentes" + render_template("primero.html" ,valorleer= diferente)
    elif int(n2)>int(n3) and int(n2)>int(n1) and diferente:
        return int(n2) + "es mayor y diferentes" + render_template("primero.html",valorleer= diferente)
    else:
        return int(n3) + "es mayor y diferentes" + render_template("primero.html",valorleer= diferente)
@app.route("/segundo")
def segundo():
    return render_template("segundo.html")
@app.route("/segundo/post", methods=["POST"])
def segundopost():

    kilo = request.form[kilo]
    if int(kilo) <= 2:
        return render_template("segundo.html", nodescuento=kilo)
    elif int(kilo) >= 2.01 and int(kilo) <= 5:
        descuento = (int(kilo)*10/100)
        return render_template("segundo.html",sidescuento= descuento)
    elif int(kilo) >= 5.01 and int(kilo) <= 10:
        desCUENTO = (int(kilo)*15/100)
        return render_template("segundo.html",sides=desCUENTO)
    else:
        DEScuento = (int(kilo)*20/100)
        return render_template("segundo.html",sedescu=DEScuento)
@app.route("/tercero")
def tercero():

    a = request.form[valora]
    b = request.form[valorb]
    c = request.form[valorc]
    d = request.form[valord]
    x = request.form[valorx]
    y = request.form[valory]

    r = int(x)*int(y)
    resultado = (int(a)*int(b))/(int(c)*int(d))
    resSULtado = (int(a)+int(b))/(int(c)+int(d))
    reSULTADO = (int(a)+int(b))-(int(c)+int(d))
    if (int(r)>0):
        return render_template("tercero.html", valor1=resultado) 
    elif (int(r)==0):
        return render_template("tercero.html", valor2=resSULtado)
    elif (int(r)<0):
        return render_template("tercero.html", valor2=reSULTADO)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
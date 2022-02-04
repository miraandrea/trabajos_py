#suma, resta, divicion, multiplicaion
from flask import Flask
app = Flask(__name__)
@app.route("/suma/<int:numero1>/<int:numero2>")
def suma(numero1,numero2):
    resultado= numero1 + numero2
    return "este es el resultado de la suma: "+ str(resultado)
@app.route("/division/<int:n1>/<int:n2>")
def division(n1,n2):
    resul= n1%n2
    return "este es el resultado de la division: "+ str(resul)
@app.route("/resta/<int:nu1>/<int:nu2>")
def resta(nu1,nu2):
    resulTADO= nu1-nu2
    return "este es el resultado de la resta: "+ str(resulTADO)
@app.route("/multiplicacion/<int:nume1>/<int:nume2>")
def multiplicacion(nume1,nume2):
    RESUL= nume1*nume2
    return "este es el resultado de la multiplicacion: "+ str(RESUL)
if __name__=="__main__":
    app.run(debug=True,port=5000)



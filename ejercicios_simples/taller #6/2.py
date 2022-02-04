from flask import Flask
app = Flask(__name__)
@app.route("/suma/<int:numero1>/<int:numero2>/")
def suma(numero1,numero2):
    resultado= numero1 + numero2
    return "este es el resultado de la suma: "+ str(resultado)
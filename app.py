from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def pagina_incial():
    return render_template("pagina_inicial.html")

@app.route('/imc', methods=["GET"])
def imc():
    nome = request.args.get("nome")
    altura = float(request.args.get("altura"))
    peso = float(request.args.get("peso"))
    imc = round((peso/altura),2)
    return render_template("imc.html", nomeuser = nome, imcuser = imc)

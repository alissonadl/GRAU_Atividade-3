from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/form_imc')
def imc():
    return render_template("form_imc.html")

@app.route('/calc_imc', methods=["GET"])
def calc_imc():
    nome = request.args.get("nome")
    altura = float(request.args.get("altura"))
    peso = float(request.args.get("peso"))
    imc = round((peso/altura**2),2)
    mensagem = ""

    if (imc < 18.5):
        mensagem = "Você está abaixo do peso."
    
    elif (imc < 24.9):
        mensagem = "Você está com o peso normal."

    elif (imc < 29.9):
        mensagem = "Você está com sobrepeso."

    else:
        mensagem = "Você está obeso."

    return render_template("calc_imc.html", mensagem = mensagem)

@app.route('/pizzaria')
def pizzaria():
    return render_template("pizzaria.html")

@app.route('/fazer_pedido')
def fazer_pedido():
    return render_template("fazer_pedido.html")

@app.route('/confirmar_pedido', methods=["POST"])
def confirmar_pedido():
    massa = request.form.get('massa')
    molho = request.form.get('molho')
    queijo = request.form.get('queijo')
    ingrediente_1 = request.form.get('ingrediente_1')
    ingrediente_2 = request.form.get('ingrediente_2')
    borda = request.form.get('borda')
    endereco = request.form.get('endereco')
    return render_template("confirmar_pedido.html", massa = massa, 
        molho = molho, queijo = queijo, ingrediente_1 = ingrediente_1, 
        ingrediente_2 = ingrediente_2, borda = borda, endereco = endereco)


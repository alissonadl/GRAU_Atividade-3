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
        mensagem = f"{nome} está abaixo do peso."
    
    elif (imc < 24.9):
        mensagem = f"{nome} está com o peso normal."

    elif (imc < 29.9):
        mensagem = f"{nome} está com sobrepeso."

    else:
        mensagem = f"{nome} está obeso."

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
    with open ("./static/txts/pedidos.txt","a") as pedidos:
        pedidos.write(f"Pedido:\n-{massa}\n-{molho}\n-{queijo}\n-{ingrediente_1}\n-{borda}\n-{endereco}\n\n")
    return render_template("confirmar_pedido.html", massa = massa, 
        molho = molho, queijo = queijo, ingrediente_1 = ingrediente_1, 
        ingrediente_2 = ingrediente_2, borda = borda, endereco = endereco)


@app.route('/temas')
def temas():
    return render_template('temas.html')

@app.route('/exibeotema', methods= ["post"])
def exibeotema():
    tipotema = request.form.get('tipotema')
    return render_template('exibeotema.html', tipotema = tipotema)

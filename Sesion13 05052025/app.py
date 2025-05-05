from flask import Flask, render_template, request, redirect, url_for
from banco import Banco

app = Flask(__name__)
banco = Banco()

@app.route('/')
def index():
    cliente_actual = banco.obtener_ultimo_cliente()
    return render_template('index.html', cliente_actual=cliente_actual)

@app.route('/ agregar' , methods=['POST'])
def agregar():
    nombre_cliente = request.form['nombre_cliente']
    banco.llegar_cliente(nombre_cliente)
    return redirect(url_for('index'))

@app.route('/atender')
def atender():
    banco.atender_cliente()
    return redirect(url_for('index'))

@app.route('/listas')
def listas():
    clientes_en_espera = banco.obtener_clientes_en_espera()
    return render_template('listas.html', clientes=clientes_en_espera)

if __name__ == '__main__':
    app.run(debug=True)
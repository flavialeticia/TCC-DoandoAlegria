from flask import Flask, render_template, flash, redirect, request, url_for, json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-palavra-secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comodoar')
def comodoar():
    return render_template('comodoar.html')

@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')

@app.route('/verongs', methods=['GET'])
def verongs():
    arquivo = open("static/ongs.json")
    ongs_dados = json.load(arquivo)
    return render_template('verongs.html', ongs_dados=ongs_dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        cadastrotipo = request.form.get('cadastrotipo')
        nomepessoa = request.form.get('nomepessoa')
        cpf = request.form.get('cpf')
        datadenascimento = request.form.get('datadenascimento')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        nomeinst = request.form.get('nomeinst')
        cnpj = request.form.get('cnpj')

        return render_template('cadastro.html', cadastrotipo=cadastrotipo)

    return render_template('cadastro.html', cadastrotipo=None)
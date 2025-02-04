from utils import db
import os
from flask_migrate import Migrate
from flask import Flask, render_template, flash, redirect, request, url_for, json
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Para o SQLite, definimos a URL de conexão do banco de dados
# Caminho absoluto para o arquivo do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\User\\Documents\\sql lite db\\db doandoalegria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db.init_app(app)
migrate = Migrate(app, db)
#

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
    with open("static/ongs.json") as arquivo:
        ongs_dados = json.load(arquivo)
    return render_template('verongs.html', ongs_dados=ongs_dados)

@app.route('/vermais/<int:index>', methods=['GET'])
def vermais(index):
    with open("static/ongs.json") as arquivo:
        ongs_dados = json.load(arquivo)
    if 0 <= index < len(ongs_dados):
        return render_template('vermais.html', instituicao=ongs_dados[index])
    else:
        return "ONG não encontrada", 404

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    cadastrotipo = "voluntario"  # Define "voluntario" como padrão

    if request.method == 'POST':
        cadastrotipo = request.form.get('cadastrotipo')
        nomepessoa = request.form.get('nomepessoa')
        cpf = request.form.get('cpf')
        datadenascimento = request.form.get('datadenascimento')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        nomeinst = request.form.get('nomeinst')
        cnpj = request.form.get('cnpj')

        # Verifica se todos os campos obrigatórios estão preenchidos
        if cadastrotipo == "voluntario":
            if all([nomepessoa, cpf, datadenascimento, email, telefone]):
                flash("Cadastro de voluntário realizado com sucesso!")
        elif cadastrotipo == "ong":
            if all([nomeinst, cnpj, email, telefone]):
                flash("Cadastro de ONG realizado com sucesso!")
                
    return render_template('cadastro.html', cadastrotipo=cadastrotipo)

@app.route('/doacao')
def doacao():
    return render_template('doacao.html')



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
        
        if email:
            flash("Mensagem")

    return render_template('cadastro.html', cadastrotipo=cadastrotipo)

@app.route('/doacao')
def doacao():
    return render_template('doacao.html')
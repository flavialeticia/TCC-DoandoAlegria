import os
from flask import Flask, render_template, flash, redirect, request, url_for, json
from datetime import datetime
from utils.db import db
from flask_migrate import Migrate
from models.voluntario import Voluntario
from models.representante_ong import Representante_ong


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Configuração do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))

#Caminho do banco de dados dentro do repositório
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db_doandoalegria.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Verifica o caminho do banco de dados
print("Caminho do banco de dados:", app.config['SQLALCHEMY_DATABASE_URI'])

# Inicializa o banco de dados e o Flask-Migrate
db.init_app(app)  # Inicializa o SQLAlchemy com a aplicação Flask
migrate = Migrate(app, db)

# Rotas
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
        return render_template('vermais.html', instituicado=ongs_dados[index])
    else:
        return "ONG não encontrada", 404

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/doacao')
def doacao():
    return render_template('doacao.html')

# Rota inicial do cadastro (escolha entre voluntário e ONG)
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para cadastro de voluntário
@app.route('/cadastro/voluntario', methods=['GET', 'POST'])
def cadastro_voluntario():
    if request.method == 'POST':
        # Coletando dados do formulário
        print(request.form.get('datadenascimento'))
        nome_completo = request.form.get('nomepessoa')
        cpf = request.form.get('cpf')
        data_nascimento = datetime.strptime(request.form.get('datadenascimento') , '%Y-%m-%d')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')

        # Validação dos campos obrigatórios
        if nome_completo and cpf and data_nascimento and email and telefone and senha:
            # Verifica se o CPF já está cadastrado
            if Voluntario.query.filter_by(cpf=cpf).first():
                flash("CPF já cadastrado. Por favor, use outro CPF.", "error")
            else:
                # Cria um novo voluntário
                novo_voluntario = Voluntario(
                    cpf=cpf,
                    nome_completo=nome_completo,
                    email=email,
                    telefone=telefone,
                    data_nascimento=data_nascimento,
                    senha=senha  # Em um cenário real, a senha deve ser hasheada
                )
                db.session.add(novo_voluntario)
                db.session.commit()
                flash("Cadastro de voluntário realizado com sucesso!", "success")
                return redirect(url_for('index'))  # Redireciona para a página inicial após o cadastro
        else:
            flash("Preencha todos os campos obrigatórios.", "error")

    return render_template('cadastro_voluntario.html')

# Rota para cadastro de ONG
@app.route('/cadastro/ong', methods=['GET', 'POST'])
def cadastro_ong():
    if request.method == 'POST':
        # Coletando dados do formulário
        nome_instituicao = request.form.get('nomeinst')
        cnpj = request.form.get('cnpj')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')

        # Validação dos campos obrigatórios
        if nome_instituicao and cnpj and email and telefone and senha:
            # Verifica se o CNPJ já está cadastrado
            if Representante_ong.query.filter_by(cnpj=cnpj).first():
                flash("CNPJ já cadastrado. Por favor, use outro CNPJ.", "error")
            else:
                # Cria uma nova ONG
                nova_ong = Representante_ong(
                    cnpj=cnpj,
                    nome_instituicao=nome_instituicao,
                    email=email,
                    telefone=telefone,
                    senha=senha  # Em um cenário real, a senha deve ser hasheada
                )
                db.session.add(nova_ong)
                db.session.commit()
                flash("Cadastro de ONG realizado com sucesso!", "success")
                return redirect(url_for('index'))  # Redireciona para a página inicial após o cadastro
        else:
            flash("Preencha todos os campos obrigatórios.", "error")

    return render_template('cadastro_ong.html')

# Execução do aplicativo
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados, se não existirem
    app.run(debug=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        #pegando dados do voluntario e representante_ong
        voluntario_atual = Voluntario.query.filter(Voluntario.email == email).first()
        representante_ong_atual = Representante_ong.query.filter(Representante_ong.email == email).first()

        if voluntario_atual != None: 
            voluntario_atual = voluntario_atual.__dict__
            if voluntario_atual['senha']== password:
                return render_template('index.html')
        
        elif representante_ong_atual != None:
            representante_ong_atual = representante_ong_atual.__dict__
            print(representante_ong_atual)
            if representante_ong_atual['senha']== password:
                return render_template('index.html')
        else:
            flash("Email ou Senha Incorretos", "error")

    return render_template('login.html')

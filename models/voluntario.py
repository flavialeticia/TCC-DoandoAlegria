from utils import db

class Voluntario(db.Model):
    __tablename__="voluntario"
    cpf = db.Column(db.String(15), primary_key = True)
    nome_completo = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(15))
    data_nascimento = db.Column(db.Date)
    senha = db.Column(db.String(20))

    def __init__(self, cpf, nome_completo, email, telefone, data_nascimento, senha):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.senha = senha
    
    def __repr__(self):
        return "<Voluntario {}>".format(self.nome_completo)

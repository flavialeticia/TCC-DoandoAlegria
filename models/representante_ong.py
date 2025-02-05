from utils.db import db

class Representante_ong(db.Model):
    __tablename__ = "representante_ong"
    cnpj = db.Column(db.String(100), primary_key=True)
    nome_instituicao = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(15))
    senha = db.Column(db.String(20))

    def __init__(self, cnpj, nome_instituicao, email, telefone, senha):
        self.cnpj = cnpj
        self.nome_instituicao = nome_instituicao
        self.email = email
        self.telefone = telefone
        self.senha = senha

    def __repr__(self):
        return "<Representante_ong {}>".format(self.nome_instituicao)
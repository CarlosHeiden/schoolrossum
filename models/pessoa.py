from main import db

#injecao de dependencia 
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(15), nullable=False)
    idade = db.Column(db.String(15), nullable=False)
    altura = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Nome%r>' % self.nome

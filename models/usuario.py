from main import db


class Usuarios(db.Model):
    nome = db.Column(db.String(15),primary_key=True, nullable=False)
    senha = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Nome%r>' % self.nome
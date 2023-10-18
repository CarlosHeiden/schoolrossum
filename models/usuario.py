from models.pessoa  import Pessoa
class Usuarios():
    def __init__(self, nome, nickname, senha):
        self.Nome = nome
        self.Nickname = nickname
        self.Senha = senha

    def __str__(self):
        return f"Nome{self.pessoa}, Nickname: {self.nickname}, Senha: {self.senha}"

        
class Pessoa:
    def __init__(self, id, nome, idade):
        self.id = id
        self.Nome = nome
        self.Idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
class Pessoa:
    def __init__(self, *filhos, idade = 'Não informada', nome=None):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return self.nome


carlos = Pessoa()
print(carlos.__dict__)
carlos.sobrenome = 'Rocha'
del carlos.filhos
print(carlos.__dict__)
karol = Pessoa()
print(karol.__dict__)

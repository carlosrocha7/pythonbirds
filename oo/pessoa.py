class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = nome    




    def cumprimentar(self):
        return 'olá'



if __name__ == '__main__':
    p = Pessoa('Filho')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)


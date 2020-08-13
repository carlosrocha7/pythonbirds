class Pessoa:
    olhos = 2

    def __init__(self, *filhos, idade = 'Não informada', nome=None):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return self.nome

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


def num_filhos():
    num=int(input('Número de filhos: '))
    return num


def filhos(num):
    lista = []
    for c in range(num):
        a=input(f'Nome do filho {c+1}: ')
        lista.append(a)
    return lista


if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    pai_filhos = Pessoa(*(renzo, filhos(num_filhos())), nome=input('Seu nome: '))
    renzo.olhos = 3
    print(f'atributos pai_filhos = {pai_filhos.__dict__}')
    print(f'atributos renzo ={renzo.__dict__}')
    print(f'Nome pai: {pai_filhos.nome}')
    print(f'Idade pai: {pai_filhos.idade}')
    print(f'Nome dos filhos: ', end='')
    print(pai_filhos.filhos[0], end=' ')
    for c in range(len(pai_filhos.filhos[1])):
        print(',', pai_filhos.filhos[1][c], end=' ')
    print()
    print(Pessoa.__dict__)
    print(Pessoa.metodo_estatico(), pai_filhos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), pai_filhos.nome_e_atributos_de_classes())




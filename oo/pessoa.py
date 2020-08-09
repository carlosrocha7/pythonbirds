'''class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome = nome




    def cumprimentar(self):
        return 'olá'



if __name__ == '__main__':
    p = Pessoa('Filho')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)'''



class Pessoa:
    def __init__(self, *filhos, idade = 'Não informada', nome=None):
        self.filhos = list(filhos)
        self.idade = idade
        self.nome = nome

    def __repr__(self):
        return self.nome



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
    print(f'Nome: {pai_filhos.nome}')
    print(f'Idade: {pai_filhos.idade}')
    print(f'Nome dos filhos: ', end='')
    print(pai_filhos.filhos[0], end=' ')
    for c in range(len(pai_filhos.filhos[1])):
        print(',', pai_filhos.filhos[1][c], end=' ')




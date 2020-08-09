
def filhos(num):
    for c in range(num):
        lista = []
        a=input(f'Nome do filho {c+1}: ')
        lista.append(a)
        print(lista)
    return lista


print(filhos(4))
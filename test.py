'''
def p(a):
    def q(b):
        def r(c):
            def s(d):
                return a+b+c+d
            return s
        return r
    return q


a = p(1)(2)(3)(4)
print(a)
'''




'''a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))


def p_decorador(func):
    def nova_func(x, y):
        return f'{func(x, y)} e {x} + {y} é igual a {x+y}'
    return nova_func


def retorna_valor(x, y):
    return f'O produto de {x} e {y} é {x*y}'


retorna_valor = p_decorador(retorna_valor)
print(retorna_valor(a, b))

# e o mesmo que abaixo

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))


def p_decorador(func):
    def nova_func(x, y):
        return f'{func(x, y)} e {x} + {y} é igual a {x+y}'
    return nova_func

@p_decorador
def retorna_valor(x, y):
    return f'O produto de {x} e {y} é {x*y}'


print(retorna_valor(a, b))
'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))


def tag(nome_tag):
    def p_decorador(func):
        def nova_func(x, y):
            return f'{nome_tag}ª operação {func(x, y)} e {x} + {y} é igual a {x+y}'
        return nova_func
    return p_decorador


@tag(1)
def retorna_valor(x, y):
    return f'O produto de {x} e {y} é {x*y}'


print(retorna_valor(a, b))

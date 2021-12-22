'''''
Faça um programa que tenha uma função chamada contador(),que receba três parâmetros: início,fim e passo e realize 
a contagem.
'''''


def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if (i < f):
        for i in range(i, f + p, p):
            print(i, end=' ')
    else:
        for i in range(i, f - p, -p):
            print(i, end=' ')


contagem(1, 10, 1)
print()
contagem(50, 20, 2)

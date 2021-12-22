'''''
Faça um programa que tenha uma função chamanda área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostra a área do terreno.
'''''


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área desse terreno de {largura} x {comprimento} é de {a}m2. ')

print('TERRENOS')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura,comprimento)




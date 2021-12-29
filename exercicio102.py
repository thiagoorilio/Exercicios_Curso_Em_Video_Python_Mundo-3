'''''
Crie um programa que tenha uma função fatorial() que receba dois parâmentros: o primeiro que indique o número
a calcular e o outro chamado show,que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de calculo do fatorial.
'''''


def fatorial(n, show=False):
    fat = 1
    for i in range(n, 0, -1):
        if show:
            print(i,end='')
            if i > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        fat *= i
    return fat




print(fatorial(4,show = True))
print(fatorial(5,show = False))
print(fatorial(9,show = True))


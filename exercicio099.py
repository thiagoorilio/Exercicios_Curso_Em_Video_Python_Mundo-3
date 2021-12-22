'''''
Faça um programa que tenha uma função chamada maior(),que receba vários parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''''
from time import sleep


def maior(*num):
    print('Analisando os valores...')
    if len(num) > 0:
        for i in num:
            print(f'{i}', end=' ')
            sleep(0.2)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
        print()
    else:
        print('Não foi digitado nenhum valor')


maior(8, 4, 2, 3, 55)
maior(2, 1, 5)
maior(37, 2, 6, 1)
maior(7, 6)
maior(5)
maior()

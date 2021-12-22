'''''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.Depois disso,mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla.
'''''
from random import randint

maior = menor = cont = 0
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for i in valores:
    print(f'{i}', end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}.')
print(f'O menor valor sorteado foi {min(valores)}')

'''''
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''''
from random import randint

numeros = list()


def sorteia():
    for i in range(0, 5):
        numeros.append(randint(0, 20))
    for n in numeros:
        print(n, end=' ')


def somaPar():
    total = 0
    soma = list()
    for p in numeros:
        if p % 2 == 0:
            soma.append(p)
    total = sum(soma)
    print(total, end=' ')


print(f'Somando os valores pares de ', end='')
sorteia()
print(',temos ', end='')
somaPar()

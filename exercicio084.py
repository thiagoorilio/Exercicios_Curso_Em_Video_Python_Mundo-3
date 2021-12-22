'''''
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final,mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''''
temp = []
pessoas = []
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = input('Deseja continuar? [S/N] ').upper()
    while resp not in 'SN':
        resp = input('Comando inválido. Deseja continuar? [S/N] ').upper()
        if resp == 'N':
            break
    if resp == 'N':
        break
print(f'Foram registradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if maior == p[1]:
        print(f'{p[0]}',end=' ')
print(f'\nAs pessoas mais leves são: ', end=' ')
for p in pessoas:
    if menor == p[1]:
        print(f'{p[0]}',end=' ')

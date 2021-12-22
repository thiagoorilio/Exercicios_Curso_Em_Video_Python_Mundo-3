'''''
Crie um programa que vai ler vários números e coloar em uma lista. Depois disso,cria duas listas extras 
que vão conter apenas os valores pares e os valores impares digitados,respectivamente. Ao final,mostre o conteúdo
das três listas geradas.
'''''
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = input('Você deseja continuar? [S/N] ').upper()
    while resp not in 'SN':
        resp = input('Comando inválido. Você deseja continuar? [S/N] ').upper()
        if resp == 'N':
            break
    if resp == 'N':
        break
print(f'Os valores da lista inteira são {lista}.')
lista_Par = lista[:]
lista_Impar = lista[:]
print(f'Os valores da lista PAR são: ', end='')
for i in lista_Par:
    if i % 2 == 0:
        print(f'{i}', end=' ')
print(f'\nOs valores da lita IMPAR são: ', end='')
for j in lista_Impar:
    if j % 2 != 0:
        print(f'{j}', end=' ')

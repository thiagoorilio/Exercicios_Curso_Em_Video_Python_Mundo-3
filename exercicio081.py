'''''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,mostre:
A)Quantos números foram digitados
B)A lista de valores,ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.
'''''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    sequencia = input('Quer continuar? [S/N] ').upper()
    while sequencia not in 'SN':
        sequencia = input('Comando inválido. Quer continuar? [S/N] ').upper()
        if sequencia == 'N':
            break
    if sequencia == 'N':
        break
print(f'Voce digitou {len(lista)} elementos. ')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

'''''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequência.
No final,mostre uma listagem de preços,organizando os dados em forma tabular.
'''''
listagem = ('Pão', 1.00, 'Arroz', 15.00, 'Queijo', 4.00, 'Presunto', 4.50, 'Nescau', 9.50)
print(f'LISTAGEM DE PREÇOS: ')
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R$: {listagem[i]:.2f} Reais')

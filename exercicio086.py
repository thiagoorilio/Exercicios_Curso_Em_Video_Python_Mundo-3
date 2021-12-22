'''''
Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final,mostre a matriz na tela,com a formatação correta.
'''''

matriz = [[], [], []]
valor = 0
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i},{j}]: '))
        matriz[i].append(valor)
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

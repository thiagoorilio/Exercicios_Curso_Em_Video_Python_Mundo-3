'''''
Aprimore o desafio anterior,mostrando no final:
A)A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha.
'''''
matriz = [[], [], []]
valor = 0
soma_todos_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i},{j}]: '))
        matriz[i].append(valor)
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            soma_todos_pares += matriz[i][j]
print(f'A soma de todos os pares é de {soma_todos_pares}.')
for i in range(0, 3):
    soma_terceira_coluna += matriz[i][2]
print(f'A soma da terceira coluna é {soma_terceira_coluna}.')
for i in range(0, 3):
    if matriz[1][i] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][i]
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')

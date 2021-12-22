'''''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.
'''''
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite um numero: '))
valores = (num1, num2, num3, num4)
print(f'O valor 9 apareceu {valores.count(9)} vez/vezes')
if 3 in valores:
    print(f'O valor 3 foi digitado na(s) posicao {valores.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ',end='')
for i in valores:
    if i % 2 == 0:
        print(f'{i}', end=' ')

'''''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,mostre qual foi o maior e o menor 
valor digitado e suas respectivas posições na lista.
'''''
valores = []
maior = []
menor = []
cont = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
print('=-' * 20)
print(f'Valores digitados são: {valores}', end='')
for pm in valores:
    if pm == max(valores):
        maior.append(cont)
    elif pm == min(valores):
        menor.append(cont)
    cont += 1
print(f'\nO maior valor guardado na lista foi {max(valores)} nas posições {maior} ')
print(f'O menor valor guardado na lista foi {min(valores)} nas posições {menor} ')

'''''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,cadastrando
tudo em uma lista composta.
'''''
from random import randint
from time import sleep
listas = [randint(1, 61)]
valor = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {valor} JOGOS ')
for i in range(1, valor + 1):
    sleep(0.5)
    print(f'Jogo {i}: {listas[i]} ')


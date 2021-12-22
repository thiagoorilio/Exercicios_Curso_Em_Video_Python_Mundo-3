"""'
Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso,de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""''
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um numero de 1 a 20: '))
while True:
    if numero > 20:
        print('Erro,Tente novamente. ', end='')
        numero = int(input('Digite um numero de 1 a 20: '))
    else:
        print(f'Voce digitou o numero {(extenso[numero])}')
        break

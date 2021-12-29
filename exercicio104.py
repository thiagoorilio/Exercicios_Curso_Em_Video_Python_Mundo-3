'''''
Crie um programa que tenha função leiaInt(), que vai funcionar de forma semelhante à função input() do python,só
que fazendo a validação para aceitar apenas um valor numérico.
'''''


def leiaInt():
    while True:
        try:
            n = int(input('Digite um numero: '))
            print(f'Voce acabou de digitar o numero {n}. ')
        except ValueError:
            print('Inadequado. Digite um numero inteiro. ')
        else:
            break


leiaInt()

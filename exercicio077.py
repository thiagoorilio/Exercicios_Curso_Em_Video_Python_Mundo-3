'''''
Crie um programa que tenha uma tupla com várias palavras (sem acentos). Depois disso, você deve mostrar
para cada palavra,quais são as suas vogais.
'''''
palavras = ('amar', 'jogar', 'programar', 'andar', 'correr', 'presente', 'trabalhar', 'gratis', 'python', 'sqlserver')
for i in palavras:
    print(f'\nNa palavra {i} temos ',end='')
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')

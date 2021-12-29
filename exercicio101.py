'''''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa,retornando um valor literal indicando se uma pessoa tem voto negado,opcional ou obrigatório
nas eleições.
'''''

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        print(f'Com {idade} anos não vota.')
    elif idade < 18 or idade >= 65:
        print(f'Com {idade} anos o voto é opcional.')
    else:
        print(f'Com {idade} anos o voto é obrigatório.')


voto(1997)
voto(2011)
voto(1950)
voto(1986)
voto(1962)
voto(2018)

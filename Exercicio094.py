'''''
Crie um programa que leia nome,sexo e idade de várias pessoas,guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com mulheres
D) Uma lista com idade acima da média
'''''
soma_idades = media_idades = 0
dicionario = dict()
lista = list()
lista_mulheres = list()
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome: ')).title()
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dicionario['sexo'] == 'F':
            lista_mulheres.append(dicionario['nome'])
        if dicionario['sexo'] in 'MF':
            break
        print('Erro. Digite apenas M/F. ')
    dicionario['idade'] = int(input('Idade: '))
    soma_idades += dicionario['idade']
    lista.append(dicionario.copy())
    resposta = input('Você deseja continuar? [S/N] ').upper()
    while resposta not in 'SN':
        resposta = input('Você deseja continuar? [S/N] ').upper()
        if resposta == 'N':
            break
    if resposta == 'N':
        break
media_idades = soma_idades / len(lista)

print('--' * 30)
print(f'Foram cadastradas {len(lista)} pessoas. ')
print(f'A média de idade do grupo é de {media_idades:.2f} anos. ')
print(f'Lista de mulheres: {lista_mulheres}.')
print(f'Pessoas acima da média de idade: ', end='')
for p in lista:
    if p['idade'] > media_idades:
        print(f'{p["nome"]}',end=' ')

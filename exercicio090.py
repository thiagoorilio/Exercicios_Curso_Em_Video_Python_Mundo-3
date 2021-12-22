'''''
Faça um programa que leia nome e média de um aluno,guardando também a situação em um dicionário.
No final,mostre o conteúdo da estrutura na tela.
'''''
dados = {}
(dados['Nome']) = str(input('Nome: '))
(dados['Media']) = float(input('Média: '))
if dados['Media'] < 7:
    (dados['Situacao']) = 'Reprovado!'
else:
    (dados['Situacao']) = 'Aprovado!'
for k, v in dados.items():
    print(f'{k} é igual a {v}')

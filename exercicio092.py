'''''
Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente,além da idade,com quantos anos a pessoa vai se aposentar.
'''''

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira_de_trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira_de_trabalho'] != 0:
    dados['ano_de_contratacao'] = int(input('Ano de contratação: '))
    dados['idade_aposentadoria'] = dados['idade'] + ((dados['ano_de_contratacao'] + 35) - datetime.now().year)
    dados['salario'] = float(input('Salário: R$ '))
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')

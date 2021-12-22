''''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,na ordem
de colocação.Depois mostre: 
A) Os 5 primeiros
B) Os 4 últimos colocados
C) Times em ordem alfabética
D)Em que posição está o time da Chapecoense
'''''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Red Bull Bragantino',
         'Fortaleza', 'Fluminense FC', 'Ceará', 'Internacional', 'América-MG',
         'Santos', 'São Paulo', 'Atlético-GO', 'Cuiabá', 'Athletico-PR', 'Bahia',
         'Juventude', 'Grêmio', 'Sport Recife', 'Chapecoense')
print(f'Lista de times: {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados do brasileirão são: {(times[0:5])}')
print('-=' * 20)
print(f'Os 4 últimos colocados do brasileirão são: {(times[16:20])}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}.')
print('-=' * 20)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}º posição')

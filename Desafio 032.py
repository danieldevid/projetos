from datetime import date
ano = int(input('\033[1;32mQue ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;32;40mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[1;31;40mO ano {} NÃO é BISSEXTO\033[m'.format(ano))


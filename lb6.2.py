'''
Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
цієї ж суми в гривнях.
Новіцька Валерія КН 122Б
'''

from enum import Enum
while True:
    class converter (Enum):
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4
    try:
        x = float (input ( 'amount of money:'))
    except ValueError:
        print('Error! Input a number.')
    p = converter [input ( 'currency (USD, EUR, CZK, PLN):')]
    if p.value == 1:
        grn = x * 24.52
        print(f'Your money in grn: {grn}')
    elif p.value == 2:
        grn = x * 26.66
        print(f'Your money in grn: {grn}')
    elif p.value == 3:
        grn = x * 1.07
        print(f'Your money in grn: {grn}')
    elif p.value == 4:
        grn = x * 6.27
        print(f'Your money in grn: {grn}')

    answer = input('Restart? Yes-1, No-2 ')
    if answer == '1':
        continue
    else:
        break

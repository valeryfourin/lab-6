'''
За s-назвою місяця визначити відповідну пору року.
Новіцька Валерія КН 122Б
'''

from enum import Enum
while True:
    class month (Enum):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12

    class season (Enum):
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4
    while True:
        try:
            s = month(int(input('Number of a month:')))
            break
        except ValueError or NameError:
            print('Error. Input number of a month 1-12.')

    if s.value in (1, 2, 12): print(f'It is {season(1).name}')
    elif s.value in (3, 4, 5): print(f'It is {season(2).name}')
    elif s.value in (6, 7, 8): print(f'It is {season(3).name}')
    elif s.value in (9, 10, 11): print(f'It is {season(4).name}')

    answer = input('Restart? Yes-1, No-2 ')
    if answer == '1':
        continue
    else:
        break
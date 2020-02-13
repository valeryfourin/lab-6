'''
Робота світлофора для водіїв запрограмована таким чином: на початку кожної
години протягом трьох хвилин горить зелений сигнал, потім протягом однієї хвилини -
жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що
минув з початку чергової години і визначає сигнал якого кольору горить для водіїв в цей
момент.
Новіцька Валерія КН 122Б
'''

from enum import Enum

while True:
    while True:
        try:
            t=int(input('Input time in minutes:'))
            break
        except ValueError or TypeError:
            print('Error. Input a number.')

    if 0<t<61:
        if 0<t%6<4: print('It is green')
        elif t%6==4: print('It is yellow')
        else: print('It is red')
    else: print('Error. Input time in minutes 1-60')

    answer = input('Restart? Yes-1, No-2 ')
    if answer == '1':
        continue
    else:
        break
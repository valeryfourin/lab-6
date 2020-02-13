'''
За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
наявність високосних років.
Новіцька Валерія КН 122Б
'''

while True:
    days = range(1, 32)
    months = range(1, 13)
    years = range(1901, 2020)
    leap_year = range(1900, 2020, 4)

    longer_month = (5, 7, 8, 10)
    short_month = (4, 6, 9, 11)
    while True:
        d = int(input ( 'day:'))
        if d not in days: print('Error. The number of a day must be 1-31')
        break
    while True:
        m = int(input ( 'month:'))
        if m not in months: print('Error. The number of a month must be 1-12')
        break
    while True:
        y = int(input( 'year:'))
        if y not in years: print('Error. The year must be 1901-2019')
        break
    prev_day = d - 1
    prev_mon = m - 1
    next_day = d + 1
    next_mon = m + 1

    if d == 1 and m in short_month:
        prev_day = 31
        print(f'The previous day is {prev_day}.{prev_mon}.{y}.')
        print(f'The next day is {next_day}.{m}.{y}')

    elif d == 1 and m == 1:
        prev_day = 31
        prev_mon = 12
        print(f'The previous day is {prev_day}.{prev_mon}.{y-1}')
        print(f'The next day is {next_day}.{m}.{y}')
    elif d == 1 and m in longer_month:
        prev_day = 30
        print(f'The previous day is {prev_day}.{prev_mon}.{y}')
        print(f'The next day is {next_day}.{m}.{y}')
    elif d == 1 and m == 3 and y not in leap_year:
        prev_day = 28
        print(f'The previous day is {prev_day}.{prev_mon}.{y}')
        print(f'The next day is {next_day}.{m}.{y}')
    elif d == 1 and m == 3 and y in leap_year:
        prev_day = 29
        print(f'The previous day is {prev_day}.{prev_mon}.{y}')
        print(f'The next day is {next_day}.{m}.{y}')
    elif (d == 31 or d == 30) and m != 12:
        next_day = 1
        print(f'The previous day is {prev_day}.{m}.{y}')
        print(f'The next day is {next_day}.{next_mon}.{y}')
    elif d == 31 and m == 12:
        next_day = 1
        next_mon = 1
        print(f'The previous day is {prev_day}.{m}.{y}')
        print(f'The next day is {next_day}.{next_mon}.{y+1}')

    answer = input('Restart? Yes-1, No-2 ')
    if answer=='1':
        continue
    else:
        break


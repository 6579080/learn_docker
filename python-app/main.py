import calendar

print('добро пожаловать в СУПЕР календарь\n')

year = int(input('пожалуйста введите год: '))
month = int(input('пожалуйста введите номер месяца: '))

print(calendar.month(year, month))

print('всего хорошего')
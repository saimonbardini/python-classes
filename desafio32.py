import calendar

year = int(input('input current year'))
if calendar.isleap(year):
    print('is leap year')
else:
    print('is not leap year')
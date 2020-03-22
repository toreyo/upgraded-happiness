#! python 3

# Detects dates in MM/DD/YYYY format.

# TODO: make regex that detects in MM/DD/YYYY format
import re
dateRegex = re.compile(r'''
(0[1-9]|1[0-2])/                  #month
(0[1-9]|1[0-9]|2[0-9]|3[0-1])/     #day
([1-2][0-9]{3})                   #year
''', re.VERBOSE)

# TODO: assign groups above to variables month, day, and year
#     write additional code that can detect if its a valid date
#      days30 = [april,june,september,november]
#       days31 = [january, march, may, july, august, october, december]
#       days28 = [february]
#           leap year special equation

# enteredDate = input('Please enter your date to determine if it is valid: ')
enteredDate = input('Please enter your date: ')
date = dateRegex.match(enteredDate)


month = date.group(1)
days = date.group(2)
year = date.group(3)

for days in month:
    days30 = ['04','06','09','11'] #April, June, September, November have 30 days
    days31 = ['01','03', '05', '07', '08', '10', '12'] #January, March, May, July, August, October, and December have 31 days
    days29 = '02'
    ly =  int(year)

    if days in days30 > str(30):
        print('Please enter a valid date')
    if days in days31 > str(31):
        print('Please enter a valid date')
    if days in days29 == str(29):
         if ly % 100 == 0 and ly % 400 == 0:
             True
         elif ly % 100 == 0:
             False
             print('Please enter a valid date')
         elif ly % 4 == 0:
             True





















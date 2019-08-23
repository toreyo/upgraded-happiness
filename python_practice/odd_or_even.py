number = int(input("Please input a number: "))
num = number % 2
num4 = num//4

if num == 1:
    print('you picked an odd number')
elif num == 0:
    print('you picked an even number')
    if num4 == 0:
        print('You picked a multiple of 4!')





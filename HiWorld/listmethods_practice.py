print('write a program to remmove duplicates in a list')

numbers = [20, 30, 50, 70, 5, 5 , 5, 7, 7, 22, 6, 22, 33, 55, 50, 33, 30]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

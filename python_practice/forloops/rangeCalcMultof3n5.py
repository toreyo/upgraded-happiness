
x = range(0,100)

def rangeCalc(r):
    total = 0
    for abc in r:
        if abc % 3 == 0 or abc % 5 == 0:
            total += abc
            print(total)

rangeCalc(x)


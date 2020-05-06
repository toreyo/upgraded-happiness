j = range(1,100)

def rangeCalc(r):
    total = 0
    for i in r:
        if i % 3 == 0:
            total += i
            print(total)

rangeCalc(j)

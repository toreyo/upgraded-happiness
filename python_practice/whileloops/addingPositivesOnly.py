posList = [10, 9, 9, 8, 7, 7, 5 ,4 ,3 ,1 , 0 , -1, -2, -2, -7, -8, -9]

posListTotal = 0
i = 0

while posList[i] > 0:
    posListTotal += posList[i]
    i+=1

print(posListTotal)

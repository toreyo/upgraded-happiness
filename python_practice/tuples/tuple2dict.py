tupleX = (('t', 3),('r', 5))
print(dict((y, x) for x, y in tupleX))


tuplex = ((2, "w"),(3, "r"), (5, "d"))
x = (dict((y, x) for x, y in tuplex))
print(x)




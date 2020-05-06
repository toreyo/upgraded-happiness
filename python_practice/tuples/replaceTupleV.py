# bad

# sample = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print((70,80,90) in sample)
#
# print(sample.index((70, 80, 90)))
#
# x, y, z = sample
# print(x)
#
# z = list(z)
# print(z)
#
# z.remove(90)
# z.append(100)
# print(z)
# z = tuple(z)
#
# sample.pop()
# sample.append(z)
# print(sample)

# good
liss = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in liss])

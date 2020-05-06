x = [5, 4, 3, 2, 1, 10, 20, 13, 5, 6, 23, 67, 75]
x.sort()
x.sort(reverse=True)

print(x)

sortedX = sorted(x)
print(sortedX)


y = ['bobby', 'Jim', 'alpha', 'Rodgers', 'jordan']
y.sort()
print(y)


sortedY = sorted(y, reverse=True)
print(sortedY)


z = [5, 4, 3, 2, 1, 10, 20, 13, 5, 6, 23, 67, 75]
print(max(z))
print(min(z))

print(sum(z))
print(sum(x+z))

x.extend(z)
print(x)


# enumerate 


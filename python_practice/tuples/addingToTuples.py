# Ways to add to tuples

tupleX = (4, 3, 2, 1)

tupleX = tupleX + (4,)
print(tupleX)

tupleX += (4, 3, 2)
print(tupleX)


tupleR = (5, 3, 2, 1, 56, 3)

tupleR += (43, 25, 6)
print(tupleR)


tupleL = [ 34, 5, 6, 2, 1]
tupleL = list(tupleL)
tupleL.extend([3, 5, 2, 1])
tupleL = tuple(tupleL)
print(tupleL)



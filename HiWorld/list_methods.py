numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

print('insert will insert a value between a range, first enter what number you would like to insert in front of, then the number you want to insert')
numbers = [5, 2, 1, 7, 4]
numbers.insert(0,10)
print(numbers)

print('remove will remove a certain value from an index')
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

print('clear will remove all numbers from an index')
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

print('pop will remove last number from index')
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

print('index will print the number in its order, within the range ')
numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))

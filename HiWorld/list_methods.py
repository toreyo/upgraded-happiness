print('append will print a number at the end')
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

print('with this code you can find if a number is in the range of numbers ')
numbers = [5, 2, 1, 7, 4]
print(50 in numbers)

print('count will show how many times a number is displayed within an index')
numbers = [5, 2, 1, 7, 4]
numbers.insert(1, 1)
print(numbers.count(1))

print('sort can also sort the numbers in a list..ascending or descending ')
numbers = [5, 2, 1, 7, 4]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print('copy can copy a list')
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()

numbers.append(30)
print(numbers)
print(numbers2)


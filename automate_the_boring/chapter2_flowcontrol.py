#comparison operators
# = assigns a value on right with variable on the left
# == asks whether two values are the same as each other

# == is equal to
# != is not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

#Boolean opeators
# and, or, not
# used to compare Boolean values
# always operate on either TRUE or FALSE

#Flow control statements
# if statements
# always end with a colon :

#elif statements
# else if statement that follows an if or elif statement

#else statements
# else clause only executed when the IF statement is false

name = input('What is your name? ')


if name == 'Alice':
    print('Hi, Alice.')
    age = int(input('What is your age? '))
    if age < 12:
        print('You are not Alice, kiddo.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are not Alice, grannie.')

#whileloops
# Will continue to loop while a condition is True
# can use break and continue statements
spam = 0
while spam <5:
    print('Hello World!')
    spam += 1

#forloops
# will loop for a certain amount of time
# can use break and continue statements

print("my name is ")
for i in range(5):
    print("Torey")

total=0
for num in range(101):
    total += num
print(total)

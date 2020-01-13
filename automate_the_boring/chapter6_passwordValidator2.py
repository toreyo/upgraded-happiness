print('Hi! Please enter your first name: \n')

while True:
    name = input()
    if name.isalpha():
        break
    else:
        print('please use only alphabets in your name')

print('Let\'s create your password! ')

while True:
    pw = input()
    if pw.isalnum():
        break
    else:
        print('please use alphabetical characters and numbers')



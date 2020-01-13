print('''Let\'s create your account!
Please input your age: 
''')
while True:
    age = input()
    if age.isdecimal():
        print('Thank you')
        break
    print('Please enter a number for your age')

print('Please create a user name!')
user_name = input()

print('Now your password. Please use both letters and numbers')

while True:
    password = input()
    if password.isalnum():
        break
    print('Please use both letters and numbers')





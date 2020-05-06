print("""
Let's drive!
type "help" to see your options""")

command=""
started=False

while True:
    command=input('>').lower()
    if command=='start':
        if started:
            print("the car is already started!!")
        else:
            started=True
            print('The car has started')


    elif command=='stop':
        if not started:
            print('The car is already stopped')
        else:
            started= False
            print('Car stoppped')

    elif command=='help':
        print("""
Type
start - to start the car
stop - to stop the car
quit - to quit the program
        """)
    elif command=="quit":
        break
    else:
        print("I don't understand what you're trying to tell meeeee")

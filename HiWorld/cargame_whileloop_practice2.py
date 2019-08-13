print('Type in "help" for a list of options to begin ur game young padawan' )

started=False
while True:
    command=input('> ').lower()


    if command=="start":
        if started:
            print('the car is already started!!!')

        print('the car has started VROOM VROOM')
    elif command=="stop":
        print('the car has stopped!')




    elif command=="help":
        print("""
type 
start- to start the game
stop - to the stop the game
quit - to exit the game""")
    elif command=="quit":
        print('the game is over')
        break
    else:
        print("I don't understand")


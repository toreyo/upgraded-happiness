import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again foo'
    elif answerNumber == 5:
        return 'Ask again latah sucka'
    elif answerNumber == 6:
        return 'Cccconcentrateeee & try again'
    elif answerNumber == 7:
        return 'No means no'
    elif answerNumber == 8:
        return 'Shit..this is not good'
    elif answerNumber == 9:
        return 'I doubt this will work'
n = 0
while n < 9:
    fortune = input('Type "fate" to show ur future > ')
    print(getAnswer(random.randint(1,9)))
    n += 1



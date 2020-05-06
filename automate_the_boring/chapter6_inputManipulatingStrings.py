print('''How are you feeling today?
 (eg. happy, sad, calm, anxious, in love, depressed) 
 ''')

feeling = input()
feeling = feeling.lower()

if feeling == 'happy':
    print('I\'m happy too!' )
elif feeling == 'sad':
    print(':( Here\'s a hug!')
elif feeling == 'calm':
    print('you had a blunt didn\'t you? ;)')
elif feeling == 'anxious':
    print("let's go to yoga together!")
elif feeling == 'in love':
    print('i love u too')
elif feeling == 'depressed':
    print('I know a great therapist!')
else:
    print('I don\'t understand that feeling')



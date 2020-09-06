#!python3
import os
import random

os.chdir(r'C:\Users\toreyoo\Desktop\upgraded-happiness\automate_the_boring\chapter8_quizzes')

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# i am a teacher making 35 quizzes, with 50 questions that will all be randomized
# question numbers are random
# question options are random

# write 35 quizzes, and quiz answers
for quizNum in range(35):
    quizQuestion = open(f'Capital Quiz {quizNum + 1}.txt', 'w')
    quizAnswer = open(f'Capital Quiz Answer {quizNum + 1}.txt', 'w')

    quizQuestion.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizQuestion.write(f'Capital Quiz Form {quizNum + 1}\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        incorrectAnswer = list(capitals.values())
        del incorrectAnswer[incorrectAnswer.index(correctAnswer)]
        incorrectAnswer = random.sample(incorrectAnswer, 3)
        answerOptions = incorrectAnswer + [correctAnswer]
        random.shuffle(answerOptions)

        quizQuestion.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n\n')
        for i in range(4):
            quizQuestion.write(f''' {'ABCD'[i]}.{answerOptions[i]}\n\n''')
        quizAnswer.write(f''' {questionNum +1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n
''')


# make the headers for the quizzes - name, date, period, title
# write the quiz questions and randomize the questions it pulls from


quizQuestion.close()
quizAnswer.close()

#! python3
#randomQuizGenerator.py - Creates quiz with questions and answers in a random order

import random

#Data of the quiz. Keys are names of the states and values correspond to their capital cities.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
'New York': 'Albany', 'North Carlina': 'Raleigh', 'North Dakota': 'Bismarck', 
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

for quizNum in range(35):
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	
	#Header for quizes
	quizFile.write('Name and surname:\n\nDate:\n\nClass:\n\n')
	quizFile.write((' ' * 20) + 'Quiz capitals of states (Quiz %s)' % (quizNum + 1))
	quizFile.write('\n\n')
	
	states = list(capitals.keys())
	random.shuffle(states)
	
	#Iterations over 50 states to prepare questions about each one
	for questionNum in range(50):
	#prepartion of correct and incorrect answers
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		#Writing questions and answers to quiz files
        quizFile.write('%s. What is a capital city of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('	%s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
		
		#Saving answers
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()
	
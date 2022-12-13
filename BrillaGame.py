print("-------------Brilla Questions Game-------------\nDeveloped by Manuel Ofosu Copyright@12/12/2022")
print('-----------------------------------------------')
print('-----------------------------------------------')
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
#User has only Two chances to get right answer
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('<<<<<Correct Answer>>>>>')
            score = score + 3 -attempt
            still_guessing = False
        elif attempt < 2:
            guess = input('Sorry, Wrong Answer. Try Again\nYour Answer: ')
            attempt += 1
        else:
            break
    print("The Correct Answer is " + answer)

score = 0
print("We Wish You GodSpeed!")

#GENERAL KNOWLEDGE QUESTIONS AND ANSWERS LIST
#GENERAL KNOWLEDGE QUESTIONS AND ANSWERS LIST
gen_quest = [
    "Which bear lives at the North Pole?\nYour Answer: ",
    "Which is the fastest land animal?\nYour Answer: ",
    "Which is the largest animal?\nYour Answer: ",
    "Which animal has a long trunk?\nYour Answer: ",
    "What kind of mammal can fly?\nYour Answer: ",
    "How many hearts does an octopus have?\nYour Answer: "]

gen_quest_answers = [
    'polar bear',
    'cheetah',
    'blue whale',
    'elephant',
    'bat',
    'three']
def generalKnowledge(quantity):
    print("GENERAL KNOWLEGE-----------------------------------")
    for i in range(quantity):
        guess = input(gen_quest[i])
        check_guess(guess, gen_quest_answers[i])
        print("-----------------------------------------------")


#MULTIPLE CHOICE QUESTIONS AND ANSWERS LIST
#MULTIPLE CHOICE QUESTIONS AND ANSWERS LIST
multple_choice = [
    'Which one of these is a fish?\nA) Whale\nB) Dolphin\nC) Shark\nD) Squid.\nType A, B, C, or D\nYour Answer: ',
    'What is the Capital of Ghana?\nA) Accra\nB) Zanziba\nC) Kumasi\nD) Gold Coast.\nType A, B, C, or D\nYour Answer: ',
    'How many days make a year?\nA) 365\nB) 365.25\nC) 360\nD) 1 Year.\nType A, B, C, or D\nYour Answer: ',
    '...is the way people live?\nA) Life\nB) Habit\nC) Culture\nD) Lifestyle.\nType A, B, C, or D\nYour Answer: ',
]

multiple_choice_Ans = ['C', 'A', 'B', 'C']

def mqc_s(quantity):
    print("MULTIPLE CHOICE------------------------------------")
    for i in range(quantity):
        guess = input(multple_choice[i])
        check_guess(guess, multiple_choice_Ans[i])
        print("-----------------------------------------------")

#TRUE OR FALSE QUESTIONS AND ANSWERS LIST
#TRUE OR FALSE QUESTIONS AND ANSWERS LIST
trueOrFalse_quest = [
    "Mice are mammals. True or False?\nYour Answer: ",
    "Water is mined at Obuasi. True or False?\nYour Answer: ",
    "Two plus minus three is equal to two square of the square root of minus one. True or False?\nYour Answer: ",
    "UG-Legon is 75 Years. True or False?\nYour Answer: ",
    "Morroco is in Europe. True or False?\nYour Answer: ",
    "Ubuntu means 'I am because we are'. True or False?\nYour Answer: "
]

trueOrFalse_answers = [
    'True',
    'False',
    'True',
    'True',
    'False',
    'True']
def trueFalse(quantity):
    print("TRUE OR FALSE--------------------------------------")
    for i in range(quantity):
        guess = input(trueOrFalse_quest[i])
        check_guess(guess, trueOrFalse_answers[i])
        print("-----------------------------------------------")

#CODE CALLING
#CODE CALLING
generalKnowledge(3)
mqc_s(3)
trueFalse(6)
print("Your Score is " + str(score))

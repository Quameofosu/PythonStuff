import random

print("-------------Nine Lives Challenge Game-------------")
print("Developed by Manuel Ofosu Copyright@15/12/2022")
print('-----------------------------------------------')
print('-----------------------------------------------')

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt',
         'otter', 'plane', 'brush', 'horse', 'light']
secret_word = random.choice(words)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1

heart_symbol = u'\u2764'
guessed_word_correctly = False

# Function to Update clue

unknown_letters = len(secret_word)


def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters


# Add difficult levels
difficulty = input(
    'Choose difficult (type 1, 2 or 3):\n 1. Easy\n 2. Normal\n 3. Hard\n Your Answer: ')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6


# Keep asking the user to guess untill they run out of lives
while lives > 0:
    print(clue)
    print('lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        unknown_letters = update_clue(
            guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
    if unknown_letters == 0:
        guessed_word_correctly = True
        break

# Determine if player won or lost

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)

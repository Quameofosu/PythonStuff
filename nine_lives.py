import random

print("-------------Nine Lives Challenge Game-------------")
print("Developed by Manuel Ofosu Copyright@15/12/2022")
print('-----------------------------------------------')
print('-----------------------------------------------')

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt',
         'otter', 'plane', 'brush', 'horse', 'light']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

# Function to Update clue


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


# Keep asking the user to guess untill they run out of lives

while lives > 0:
    print(clue)
    print('lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1

# Determine if player won or lost

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)

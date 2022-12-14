from pyqrcode import QRCode
import random
import string
import pyqrcode
#import webbrowser

adjectives = ['slpy', 'sxlw', 's+mly', 'w.et', 'fVat',
              'r^d', 'org~', 'F;y3{', 'L=Zn', 'bJK"', 'purple', 'fluffy',
              'white', 'proud', 'brave', 'strong', 'wi,/ld%', '|mo]dy', '.bl?k', 'cAo:#']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda',
         'telephone', 'banana', 'teacher']


print("Welcome to Password Picker!")
print()
while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        special_char1 = random.choice(string.punctuation)

        password = adjective + \
            str(number) + special_char1 + noun + str(number) + special_char
        print("Your new password is: %s" % password)

    respond = input("Would you like another password? Type y or n: ")
    if respond == 'n':
        break

# webbrowser.open_new('https://www.youtube.com/watch?v=iR2hYpq0KI0')

# QR code generator


# String which represent the QR code
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myyoutube.svg", scale=8)

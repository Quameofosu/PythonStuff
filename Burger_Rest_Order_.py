print("Welcome to Grillby’s Burger Restaurant ")
burger_options = ['Regular', 'Glutten-free', 'Veggie',
                  'Impossible burger', 'Royale', 'Vegan-Only']
answer_num = [1, 2, 3, 4, 5, 6]

print("----------This is our Menu----------")
print("1. Regular\n2. Glutten-free\n3. Veggie\n4. Impossible burger\n5. Royale\n6. Vegan-Only\n\nType Numbers Only")

heart_symbol = u'\u2764 '
user_input = input(
        'What kind of Burger and burn do you want?\nYour Answer: ')


"""

while True:
    try:
        if int(user_input) in answer_num:
            break
            #print("You selected {}".format(user_input))
        break
    except ValueError:
        while True:
            user_input = input(
        'What kind of Burger and burn do you want?\nYour Answer: ')
            try:
                if int(user_input) in answer_num:
                    print("{} Hurray, you made it".format(heart_symbol))
                break
            except ValueError:
                print("Try Again, Enter a Number")
                break


"""

        
while True:
    text = input("Please enter a text between 1 and 6: ")
    if text.isdigit() and 1 <= int(text) <= 6:
        # This text is a valid number between 1 and 6
        break
    else:
        #The text is not a valid number between 1 and 6
        print("Invalid input. Please try again.")


print('Heello Me')

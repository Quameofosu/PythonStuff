print("Welcome to Grillby’s Burger Restaurant ")
burger_options = ['Regular', 'Glutten-free', 'Veggie',
                  'Impossible burger', 'Royale', 'Vegan-Only']
answer_num = [1, 2, 3, 4, 5, 6]

print("----------This is our Menu----------")
print("1. Regular\n2. Glutten-free\n3. Veggie\n4. Impossible burger\n5. Royale\n6. Vegan-Only\n\nType Numbers Only")

i = 1

while (i < 7):
    user_input = input(
        'What kind of Burger and burn do you want?\nYour Answer: ')
    if user_input == answer_num[i]:
        print("You selected {}".format(user_input))
    else:
        print("Please enter a valid option")
    i += i

print('Heelo Me')

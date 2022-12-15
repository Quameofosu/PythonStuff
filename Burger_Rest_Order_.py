print("Welcome to Grillby’s Burger Restaurant ")
burger_options = ['Regular', 'Glutten-free', 'Veggie',
                  'Impossible burger', 'Royale', 'Vegan-Only']
print("----------This is our Menu----------")
print("1. Regular\n2. Glutten-free\n3. Veggie\n4. Impossible burger\n5. Royale\n6. Vegan-Only")

i = 0
answer_num = [1, 2, 3, 4, 5, 6]

user_input = input(
    'What kind of Burger and burn do you want?\nYour Answer: ')

while (i < 6):
    if answer_num or burger_options[i]:
        print("You chose ", user_input)
        break
    else:
        print("Please enter a valid option")
        user_input = input(
            'What kind of Burger and burn do you want?\nYour Answer: ')
    break

print('Heelo Me')

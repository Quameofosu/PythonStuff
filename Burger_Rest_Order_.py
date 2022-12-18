print("Welcome to Grillby’s Burger Restaurant ")
burger_options = ['Regular', 'Glutten-free', 'Veggie',
                  'Impossible burger', 'Royale', 'Vegan-Only']
answer_num = [1, 2, 3, 4, 5, 6]

print("----------This is our Menu----------")
print("1. Regular\n2. Glutten-free\n3. Veggie\n4. Impossible burger\n5. Royale\n6. Vegan-Only\n\nType Numbers Only")


user_input = input(
        'What kind of Burger and burn do you want?\nYour Answer: ')

while True:
    try:
        if int(user_input) in answer_num:
            print("You selected {}".format(user_input))
        break
    except ValueError:
        print("Please Enter a Number")


print('Heello Me')

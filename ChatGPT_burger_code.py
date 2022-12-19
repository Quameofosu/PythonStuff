"""

"""

# Constants for the possible burger and bun options
BURGER_OPTIONS = ["Regular", "Gluten-free", "Veggie", "Impossible burger", "Royale"]
BUN_OPTIONS = ["Regular", "Gluten-free", "Vegan"]

# Greet the user
print("Welcome to Grillby's online order system!")

# Initialize variables to store the user's selection
selected_burger = ""
selected_bun = ""

# Keep asking the user for their burger and bun selection until they enter a valid option
while selected_burger not in BURGER_OPTIONS or selected_bun not in BUN_OPTIONS:
  # Ask the user for their burger selection
  selected_burger = input("Please select a burger: ")

  # If the user's burger selection is not in the list of possible options, ask them to try again
  if selected_burger not in BURGER_OPTIONS:
    print("Invalid burger selection. Please try again.")

  # Ask the user for their bun selection
  selected_bun = input("Please select a bun: ")

  # If the user's bun selection is not in the list of possible options, ask them to try again
  if selected_bun not in BUN_OPTIONS:
    print("Invalid bun selection. Please try again.")

# Print the user's final selection
print("You have selected a " + selected_burger + " burger on a " + selected_bun + " bun.")





"""
To modify the program to ask the user for their toppings and keep track of their selections, you can use a while loop and a list to keep track of the toppings entered by the user. The while loop should keep asking the user for new toppings until they enter the word "done". You can use the in operator to check if a topping has already been entered by the user. If the user enters a topping that is already in the list, you can ask them to enter a different topping. If the user enters a valid topping that is not already in the list, you can add it to the list.

Here is how you can modify the program to ask the user for their toppings and keep track of their selections:

"""
# Constants for the possible burger and bun options
BURGER_OPTIONS = ["Regular", "Gluten-free", "Veggie", "Impossible burger", "Royale"]
BUN_OPTIONS = ["Regular", "Gluten-free", "Vegan"]

# Constant for the possible topping options
TOPPING_OPTIONS = ["Lettuce", "Tomato", "Onion", "Pickle", "Ketchup", "Mustard", "Mayonnaise"]

# Greet the user
print("Welcome to Grillby's online order system!")

# Initialize variables to store the user's selection
selected_burger = ""
selected_bun = ""
selected_toppings = []

# Keep asking the user for their burger and bun selection until they enter a valid option
while selected_burger not in BURGER_OPTIONS or selected_bun not in BUN_OPTIONS:
  # Ask the user for their burger selection
  selected_burger = input("Please select a burger: ")

  # If the user's burger selection is not in the list of possible options, ask them to try again
  if selected_burger not in BURGER_OPTIONS:
    print("Invalid burger selection. Please try again.")

  # Ask the user for their bun selection
  selected_bun = input("Please select a bun: ")

  # If the user's bun selection is not in the list of possible options, ask them to try again
  if selected_bun not in BUN_OPTIONS:
    print("Invalid bun selection. Please try again.")

# Initialize a variable to keep track of whether the user is done selecting toppings
done = False

# Keep asking the user for toppings until they enter "done"
while not done:
  # Ask the user for a topping
  topping = input("Please enter a topping, or type 'done' if you are finished: ")

  # If the user has entered "done", set the done flag to True
  if topping.lower() == "done":
    done = True
  # If the user has entered a topping that is not in the list of possible options, ask them to try again
  elif topping not in TOPPING_OPTIONS:
    print("Invalid topping. Please try again.")
  # If the user has entered a topping that is already in the list of selected toppings, ask them to try again
  elif topping in selected_toppings:
    print("This topping has already been selected. Please select a different topping.")
  # If the user has entered a valid topping that is not already in the list of selected toppings, add it to the list



"""
To output the receipt for the user's order, you can use the information that has been collected about the user's selections and the base costs for each type of burger and bun. You can use a list to maintain the base costs for each type, in the same order as the earlier global variable.

To calculate the total cost of the order, you can iterate over the list of selected toppings and add the appropriate cost for each topping. The first two toppings are free, but any additional topping costs $1.25, except for kimchi, which costs $5. If the user has selected kimchi as one of the first two toppings, then the other of the two and the third topping will be the two free toppings.

Here is how you can output the receipt for the user's order:

"""

# Constants for the possible burger and bun options
BURGER_OPTIONS = ["Regular", "Gluten-free", "Veggie", "Impossible burger", "Royale"]
BUN_OPTIONS = ["Regular", "Gluten-free", "Vegan"]

# Constant for the possible topping options
TOPPING_OPTIONS = ["Lettuce", "Tomato", "Onion", "Pickle", "Ketchup", "Mustard", "Mayonnaise", "Kimchi"]

# List of base costs for each type of burger and bun
BASE_COSTS = [5.99, 6.99, 7.99, 8.99, 9.99, 1.99, 2.99, 3.99]

# Greet the user
print("Welcome to Grillby's online order system!")

# Initialize variables to store the user's selection
selected_burger = ""
selected_bun = ""
selected_toppings = []

# Keep asking the user for their burger and bun selection until they enter a valid option
while selected_burger not in BURGER_OPTIONS or selected_bun not in BUN_OPTIONS:
  # Ask the user for their burger selection
  selected_burger = input("Please select a burger: ")

  # If the user's burger selection is not in the list of possible options, ask them to try again
  if selected_burger not in BURGER_OPTIONS:
    print("Invalid burger selection. Please try again.")

  # Ask the user for their bun selection
  selected_bun = input("Please select a bun: ")

  # If the user's bun selection is not in the list of possible options, ask them to try again
  if selected_bun not in BUN_OPTIONS:
    print("Invalid bun selection. Please try again.")

# Initialize a variable to keep track of whether the user is done selecting toppings
done = False

# Keep asking the user for toppings until they enter "done"
while not done:
  # Ask the user for a topping
  topping = input("Please enter a topping, or type 'done' if you are finished: ")

  # If the user has entered "done", set the done flag to True
  if topping.lower() == "done":
    done = True
  # If the user has entered a topping that is not in the list of possible options, ask them to try again
  elif topping not in TOPPING_OPTIONS:
    print("Invalid topping. Please try again.")
  # If the user has entered a



  """
  Here is the modified program that includes the code to output the receipt for the user's order:

  """

# Constants for the possible burger and bun options
BURGER_OPTIONS = ["Regular", "Gluten-free", "Veggie", "Impossible burger", "Royale"]
BUN_OPTIONS = ["Regular", "Gluten-free", "Vegan"]

# Constant for the possible topping options
TOPPING_OPTIONS = ["Lettuce", "Tomato", "Onion", "Pickle", "Ketchup", "Mustard", "Mayonnaise", "Kimchi"]

# List of base costs for each type of burger and bun
BASE_COSTS = [5.99, 6.99, 7.99, 8.99, 9.99, 1.99, 2.99, 3.99]

# Greet the user
print("Welcome to Grillby's online order system!")

# Initialize variables to store the user's selection
selected_burger = ""
selected_bun = ""
selected_toppings = []

# Keep asking the user for their burger and bun selection until they enter a valid option
while selected_burger not in BURGER_OPTIONS or selected_bun not in BUN_OPTIONS:
  # Ask the user for their burger selection
  selected_burger = input("Please select a burger: ")

  # If the user's burger selection is not in the list of possible options, ask them to try again
  if selected_burger not in BURGER_OPTIONS:
    print("Invalid burger selection. Please try again.")

  # Ask the user for their bun selection
  selected_bun = input("Please select a bun: ")

  # If the user's bun selection is not in the list of possible options, ask them to try again
  if selected_bun not in BUN_OPTIONS:
    print("Invalid bun selection. Please try again.")

# Initialize a variable to keep track of whether the user is done selecting toppings
done = False

# Keep asking the user for toppings until they enter "done"
while not done:
  # Ask the user for a topping
  topping = input("Please enter a topping, or type 'done' if you are finished: ")

  # If the user has entered "done", set the done flag to True
  if topping.lower() == "done":
    done = True
  # If the user has entered a topping that is not in the list of possible options, ask them to try again
  elif topping not in TOPPING_OPTIONS:
    print("Invalid topping. Please try again.")
  # If the user has entered a topping that is already in the list of selected toppings, ask them to try again
  elif topping in selected_toppings:
    print("This topping has already been selected. Please select a different topping.")
  # If the user has entered a valid topping that is not already in the list of selected toppings, add it to the list
  else:
    selected_toppings.append(topping)

# Calculate the total cost of the order
total_cost = BASE_COSTS[BURGER_OPTIONS.index(selected_burger)] + BASE_COSTS[BUN_OPTIONS.index(selected_bun) + len(BURGER_



"""
To meet the requirements of the question, you can refactor the program to define separate functions for each part of the process, and then call these functions as appropriate in a main() function. You can use doctest to test your functions.

Here is an example of how you can refactor the program to meet these requirements:

"""

import doctest

def main():
    """
    >>> main()
    Welcome to Grillby's online order system!
    Please select a burger: Regular
    Please select a bun: Gluten-free
    Please enter a topping, or type 'done' if you are finished: Lettuce
    Please enter a topping, or type 'done' if you are finished: Tomato
    Please enter a topping, or type 'done' if you are finished: Onion
    Please enter a topping, or type 'done' if you are finished: Pickle
    Please enter a topping, or type 'done' if you are finished: Ketchup
    Please enter a topping, or type 'done' if you are finished: Mustard
    Please enter a topping, or type 'done' if you are finished: Mayonnaise
    Please enter a topping, or type 'done' if you are finished: done
    You have selected a Regular burger on a Gluten-free bun with the following toppings: Lettuce, Tomato, Onion, Pickle, Ketchup, Mustard, Mayonnaise.
    The total cost of your order is $7.99.
    """
    # Greet the user
    print("Welcome to Grillby's online order system!")

    # Get the user's burger and bun selection
    selected_burger, selected_bun = get_burger_and_bun_selection()

    # Get the user's toppings selection
    selected_toppings = get_toppings_selection()

    # Print the user's final selection
    print(f"You have selected a {selected_burger} burger on a {selected_bun} bun with the following toppings: {', '.join(selected_toppings)}.")

    # Calculate and print the total cost of the order
    total_cost = calculate_total_cost(selected_burger, selected_bun, selected_toppings)
    print(f"The total cost of your order is ${total_cost:.2f}.")

def get_burger_and_bun_selection():
    """
    >>> get_burger_and_bun_selection()
    ('Regular', 'Gluten-free')
    """
    # Constants for the possible burger and bun options
    BURGER_OPTIONS = ["Regular", "Gluten-free", "Veggie", "Impossible burger", "Royale"]
    BUN_OPTIONS = ["Regular", "Gluten-free", "Vegan"]

    # Initialize variables to store the user's selection
    selected_burger = ""
    selected_bun = ""

    # Keep asking the user for their burger and bun selection until they enter a valid option
    while selected_burger not in BURGER_OPTIONS or selected_bun not in BUN_OPTIONS:
        # Ask the user for their burger selection
        selected_burger = input("Please select a burger: ")

        # If the user's burger selection is not in the list of possible options, ask them to try again
        if selected



"""
Here is the rest of the refactored program:

"""

import doctest

def main():
    """
    >>> main()
    Welcome to Grillby's online order system!
    Please select a burger: Regular
    Please select a bun: Gluten-free
    Please enter a topping, or type 'done' if you are finished: Lettuce
    Please enter a topping, or type 'done' if you are finished: Tomato
    Please enter a topping, or type 'done' if you are finished: Onion
    Please enter a topping, or type 'done' if you are finished: Pickle
    Please enter a topping, or type 'done' if you are finished: Ketchup
    Please enter a topping, or type 'done' if you are finished: Mustard
    Please enter a topping, or type 'done' if you are finished: Mayonnaise
    Please enter a topping, or type 'done' if you are finished: done
    You have selected a Regular burger on a Gluten-free bun with the following toppings: Lettuce, Tomato, Onion, Pickle, Ketchup, Mustard, Mayonnaise.
    The total cost of your order is $7.99.
    """
    # Greet the user
    print("Welcome to Grillby's online order system!")

    # Get the user's burger and bun selection
    selected_burger, selected_bun = get_burger_and_bun_selection()

    # Get the user's toppings selection
    selected_toppings = get_toppings_selection()

    # Print the user's final selection
    print(f"You have selected a {selected_burger} burger on a {selected_bun} bun with the following toppings: {', '.join(selected_toppings)}.")

    # Calculate and print the total cost of the order
    total_cost = calculate_total_cost(selected_burger, selected_bun, selected_toppings)
    print(f"The total cost of your order is ${total_cost:.2f}.")

def get_burger_and_bun_selection():
    """
    >>> get_burger_and_bun_selection()
    ('Regular

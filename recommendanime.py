from restaurantData import restaurant_data, types
from recommendfunctions.functions import *

sorted_types = quick_sort(types)
organized_restaurants = restaurant_dictionary(restaurant_data)

def main():
    while True:
        food_type = input("What kind of food would you like?\nEnter first letter: ").strip().lower()
        try:
            type_choices = type_dictionary(sorted_types)[food_type]
        except KeyError as e:
            print(f"Sorry, {e} is not a valid input.")
        else:
            break

    print(f"Your options are: {type_choices}")

    type_choice = input("Which one would you like?\nEnter name: ").strip().lower()
    while True:
        if type_choice in type_choices:
            confirmation = input(f"Would you like to view {type_choice} restaurants?\ny/n: ").strip().lower()
            break
        else:
            print("That option was not listed.")
        type_choice = input("Which one would you like?\nEnter name: ").strip().lower()


    while True:
        if confirmation == 'y':
            print(f"The {type_choice} restaurants are: ")
            print(organized_restaurants[type_choice])
            while True:
                search = input(" Would you like to continue your search?\ny/n: ").strip().lower()
                if search == 'y':
                    main()
                elif search == 'n':
                    print("Okay! Goodbye...")
                    quit()
        elif confirmation == 'n':
            print("Okay!", end="")
            while True:
                search = input(" Would you like to continue your search?\ny/n: ").strip().lower()
                if search == 'y':
                    main()
                elif search == 'n':
                    print("Okay! Goodbye...")
                    quit()
        else:
            print("That was not an option.")
            confirmation = input(f"Would you like to view {type_choice} restaurants?\ny/n: ").strip().lower()

print("Welcome to Codecademy Project Placeholder")
main()
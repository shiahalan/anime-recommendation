from restaurantData import restaurant_data, types
from recommendfunctions.functions import *

sorted_types = quick_sort(types)



print("Welcome to Codecademy Project Placeholder")
food_type = input("What kind of food would you like?\nEnter first letter: ").strip().lower()
print(type_dictionary(sorted_types)[food_type])

#!/usr/bin/env python3

def get_pizza():
     """ This code demonstrates how dict can be used as in Switch case statement. Since Switch case is not there in python.
     """
     pizza_dict = { 'Monday' : 'Veggie_Crust',
                    'Tuesday' : 'Mushroom',
                    'Wednesday' : 'Taco',
                    'Thursday' : 'Spinach',
                    'Friday' : 'Egg_plant',
                    'Saturday' : 'Bell_pepper',
                    'Sunday' : 'Onion_Tomato' }
     day = input("Please enter today's day in the form of Sunday or Monday: ")
     my_pizza = pizza_dict[day]
     print(f"Ordering {my_pizza} pizza now....")

if __name__ == '__main__':
    get_pizza()

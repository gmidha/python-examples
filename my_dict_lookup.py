#!/usr/bin/env python3

def main():
    """ This program displays the lookup of an item in a dictionary.
    """
    my_dict = { 'Gaurav' : 123456,
                 'Rohit' : 345789,
                 'Sunny' : 657908,
                 'Tony'  : 789098,
                 'Sony'  : 876987 }
    key = input("Enter a name to find his/her phone number: ")

    for name,num in my_dict.items():
         if name == key:
             print(f"{name}'s phone number is: {num}")

if __name__ == "__main__":
    main()

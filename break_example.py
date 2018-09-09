#!/usr/bin/env python3

""" This program demonstrates the usage of for loop with break statement. It will try to fill the cabinet with dishes until there is a space. """

from random import randint

def fill_cabinet():
    dishwasher = ['plate', 'bowl', 'spoon', 'knife', 'big bowl', 'small bowl',
                  'plate', 'bowl', 'spoon', 'knife', 'big bowl', 'small bowl',
                  'plate', 'bowl', 'spoon', 'knife', 'big bowl', 'small bowl']
    for item in list(dishwasher):    #creating a copy of dishwasher list using list()
        if not randint(0, 19):
            print("You are out of Space")
            break
        else:
            print(f"Adding {item} to the Cabinet.")
            dishwasher.remove(item)

if __name__ == "__main__":
    fill_cabinet()

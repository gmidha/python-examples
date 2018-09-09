#!/usr/bin/env python3

""" This program demonstrates the uasge of stack where we are adding items and following "Last In, First Out". We are going to use list in this example. We are using append() and    pop method of the list to add and access items.
"""

def create_stack():
    stack = list()
    stack.append('bill1')
    stack.append('bill2')
    stack.append('bill3')
    stack.append('bill4')
    print("Items in my stack are: ")
    for item in range(len(stack)):
        print(f"{stack.pop()}")

if __name__ == '__main__':
    create_stack()

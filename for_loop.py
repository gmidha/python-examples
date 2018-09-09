#!/usr/bin/env python3

def clean_dishes():
    """ This program demonstrates the usage of for loop with list.
    """
    sink = ['plate', 'pot', 'glass', 'cooker']
    print(f"Sink contains these dirty dishes: {sink}")
    for item in list(sink):   #creating a copy of sink list to iterate through it
        print(f"adding {item} into the dishwasher")
        sink.remove(item)

if __name__ == '__main__':
    clean_dishes()

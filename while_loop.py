#!/usr/bin/env python3

# Cleanning a Stubborn Dirty Pan

from random import randint

def clean_pan():
    """ This function cleans a stubborn dirty pan
    """
    dirty = True   #pan is dirty
    clean_counts = 0
    while dirty:
        clean_counts += 1
        print(f"Rinse and wash the dirty pan for count: {clean_counts}")
        if not randint(0,9): # this if will run only when random.randint returns 0. if it returns zero, then pan is clean.
            dirty = False
            print(f"pan is clean now, we did it in {clean_counts} counts")

if __name__ == '__main__':
    clean_pan()

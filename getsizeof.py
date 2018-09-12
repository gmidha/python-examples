#!/usr/bin/env python3

""" This program demonstrates the usage of getsizeof function of sys module. It will print the size of the list and not the refrenced object.
"""

import sys

if __name__ == "__main__":
    n = int(input("Enter the size of list: "))
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length is {a}; Size in bytes is {b}")
        data.append(None)

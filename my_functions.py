#!/usr/bin/env python3

# This program demonstrates the usage of any, all, sum, max and min functions.

def main():

    list = [1, 3, 6, 9, 0, 10]
    # any function returns true if list has a value that is true
    print(f"any: {any(list)}")
    print("-----------")

    # all function returns true is list has all the values equal to true
    print(f"all: {all(list)}")
    print("-----------")

    # sum function returns total sum of all the elements in the list
    print(f"sum: {sum(list)}")
    print("-----------")

    # max function returns max of all the elements in the list
    print(f"max: {max(list)}")
    print("-----------")

    # min function returns min of all the elements in the list
    print(f"min: {min(list)}")
    print("-----------")

if __name__ == "__main__":
    main()

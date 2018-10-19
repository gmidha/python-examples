#!/usr/bin/env python3

# This program calculates factorial using recursion.

def factorial(num):
    if num == 0:
       return 1
    else:
       return num*factorial(num-1)

def main():
    print(factorial(5))

if __name__ == "__main__":
    main()

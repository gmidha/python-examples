#!/usr/bin/env python3
# this program figures out whether a number is odd or even number

def odd_or_even():
    x = int(input("Enter a number: "))
    print("{} number is even".format(x)) if x % 2 == 0 else print("{} number is odd".format(x))

def main():
    odd_or_even()

if __name__ == '__main__':
    main()

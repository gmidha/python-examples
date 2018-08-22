#!/usr/bin/env python3

def get_numbers():
    x = int(input("enter first number: "))
    y = int(input("enter second number: "))
    return x,y

def divisible():
    a,b = get_numbers()
    print(f"{a} is divisible by {b}") if a % b == 0 else print(f"{a} is not divisible by {b}")

def main():
    divisible()

if __name__ == '__main__':
    main()

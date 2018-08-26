#!/usr/bin/env python3
#this program gets a number as input from a user and prints the divisors for that number.
def get_number():
    x = int(input("Enter a number: "))
    return x

def divisor():
    div = get_number()
    divisors = []
    for n in range(1, div+1 ):
        if div % n == 0:
            divisors.append(n)
    print(f"{divisors}")

if __name__ == "__main__":
    divisor()

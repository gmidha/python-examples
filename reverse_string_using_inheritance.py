#!/usr/bin/env python3

# This program demonstrates the usage of inheritance for reversing a string

class Revstr(str):

    def __str__(self):
        return self[::-1]


def main():

    hello = Revstr('hello world')
    print(f'{hello}')


if __name__ == "__main__":

    main()

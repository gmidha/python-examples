#!/usr/bin/env python3

# This program demonstrates the usage of a simple class Flower that stores the following data variables: 1. name 2. number of petals and 3. price

class Flower:

    def __init__(self, name, num_petals, price):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self):
        return self._name

    def get_num_petals(self):
        return self._num_petals

    def get_price(self):
        return self._price

def main():
    f = Flower('Rose', 16, 4.0)
    print(f"Flower name is: {f.get_name()}")
    print(f"Flower's petals are: {f.get_num_petals()}")
    print(f"Flower's price is: {f.get_price()}")

if __name__ == "__main__":
    main()

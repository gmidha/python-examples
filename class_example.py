#!/usr/bin/env python3

# This program demonstrates the usage of Class in python

class Duck:

    sound = "quack... quack"
    movement = "move like a duck.."

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():

    Donald = Duck()
    Donald.quack()
    Donald.move()

if __name__ == "__main__":

    main()

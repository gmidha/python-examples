#!/usr/bin/env python3

# This program demonstrates the usage of Animal class with __str__() special method which returns string for an object.

class Animal:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else "dog"
        self._name = kwargs['name'] if 'name' in kwargs else "Tommy"
        self._sound = kwargs['sound'] if 'sound' in kwargs else "woffwoff"

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

    def __str__(self):
        return f'{self.type()} -- {self.name()} -- {self.sound()}'

def main():
    a0 = Animal(type='Kitten', name='kity', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')

    print(a1)
    print(a0)
    print(Animal())

if __name__ == '__main__':
    main()

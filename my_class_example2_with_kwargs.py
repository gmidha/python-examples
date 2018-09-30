#!/usr/bin/env python3

# This program demonstrates the usage of **kwargs with default values in  Animal class.

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

def print_animal(obj):
     if not isinstance(obj, Animal):
         raise TypeError("print_animal requires an Animal object")
     print(f"{obj.type()} -- {obj.sound()} -- {obj.name()}")

def main():
    a0 = Animal(type='Kitten', name='kity', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')

    print_animal(a1)
    print_animal(a0)
    print_animal(Animal())

#!/usr/bin/env python3

# This program demonstrates Inheritance of Animal class.

class Animal:

    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

    def __str__(self):
        return f'{self.type()} -- {self.name()} -- {self.sound()}'

class Duck(Animal):

    def __init__(self, **kwargs):

        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs) #Call inherited class's init method

class Kitten(Animal):

    def __init__(self, **kwargs):

        self._type = 'Kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs) #Call inherited class's init method

def main():
    a0 = Kitten(name='kity', sound='rwar')
    a1 = Duck(name='donald', sound='quack')

    print(a1)
    print(a0)

if __name__ == '__main__':
    main()

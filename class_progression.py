#!/usr/bin/env python3

# This program demonstrates the usage of Progression class and then use it as a base class for AirthmeticProgression, GeometricProgression and Fibonacci Progression series

class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration("No More elements are present")
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class AirthmeticProgression(Progression):
    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):
    def __init__(self, start=1, base=2):
        super().__init__(start)
        self._base = base

    def _advance(self):
         self._current *= self._base

class Fibonacci(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

def main():
    print("Airthmetic progression: ")
    a = AirthmeticProgression(1, 2)
    a.print_progression(10)
    print("Geometric series: ")
    g = GeometricProgression(1, 4)
    g.print_progression(10)
    print("Fibonacci series: ")
    f = Fibonacci(1, 10)
    f.print_progression(10)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class Vector:
    # This class demonstrates the usage of special named methods and vector implementation
    def __init__(self, d):
        self._v = [0] * d

    def __len__(self):
        return len(self._v)

    def __getitem__(self, k):
         return self._v[k]

    def __setitem__(self, j, val):
         self._v[j] = val

    def __str__(self):
         return '<' + str(self._v)[1:-1] + '>'
         
    def __add__(self, other):
         if len(self._v) != len(other._v):
             raise ValueError('Dimension must match')
         result = Vector(len(self._v))
         for j in range(len(self._v)):
              result[j] = self._v[j] + other._v[j]
         return result

def main():
    a = Vector(3)
    a[2] = 45
    a[0] = 21
    print(a[0])
    print(a[1])
    print(a[2])
    print(a)
    b = a + a
    print(b)

if __name__ == "__main__":
    main()

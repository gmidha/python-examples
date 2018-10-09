#!/usr/bin/env python3

# This Program demonstrates the usage of Range class.

class Range:

    def __init__(self, start, stop=None, step=1):

        if step == 0:
            raise ValueError("Step value cannot be zero.")

        if stop == None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1)//step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k<0:
            k += self._length

        if not 0<=k<self._length:
            raise IndexError("Index value should be between 0 and length")

        return self._start + k * self._step

def main():
    r = Range(2,100,1)
    for i in r:
        print(f"{i}", end=" ")

if __name__ == '__main__':
    main()

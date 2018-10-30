#!/usr/bin/env python3

#This example demonstrates the growth of size of a list

import sys

def main():
    data = []
    for k in range(100):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"{a} length of data has size {b}")
        data.append(None)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# This program demonstrates the reading of file "lines.txt" and displaying the lines.

def main():
    fd = open('lines.txt')
    for line in fd:
        print(line.rstrip()) #rstrip removes the extra "end of line".

if __name__ == "__main__":
    main()

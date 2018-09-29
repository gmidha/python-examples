#!/usr/bin/env python3

# This example demonstrates bytes vs string

def main():

    print("Bytes are:")
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(f"{b}")

    print("String is: ")
    s = "This is my string"
    print(f"{s}")

if __name__ == "__main__":
    main()

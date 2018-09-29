#!/usr/bin/env python3

# This example demonstrates bytes vs string

def main():

    print("Bytes are:")
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(f"{b}")

    print("String is: ")
    s = "This is my string"
    print(f"{s}")

    #print(s+b) #this will not work because print expects a string and we are having bytes. We will have to decode it first.
    s2 = b.decode('utf-8')
    print(s+s2)
    
    # We can also encode string to bytes using encode function
    b2 = s.encode('utf-8')
    print(b+b2) #since both are bytes, print will convert those in string.

if __name__ == "__main__":
    main()

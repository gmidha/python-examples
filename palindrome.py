#!/usr/bin/env python3
# This script gets input from user and checks whether it is palindrome or not.

def get_string():
    """ This function gets a string as user input.
    """
    str = input("Please enter a String: ")
    return str

def check_palindrome():
    """This function checks whether
       the input string returned from get_string is palindrome or not.
    """
    k = -1
    j = 0
    my_str = get_string()
    for i in range(len(my_str)):
        if my_str[k] != my_str[i]:
            j = -1
            print(f"{my_str} is not palindrome")
            exit()
        else:
            k -= 1
            j = 0
    if j == 0:
        print(f"{my_str} is palindrome")
        
if __name__ == "__main__":
    check_palindrome() 

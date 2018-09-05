#!/usr/bin/env python3

def main():
    """  This program displays the usage of sets that stores unique items as
         an unordered list.
    """
    college = set(['Gaurav', 'Lokesh', 'Ankit', 'Kirti', 'Gagan'])
    coworkers = set(['Santhosh', 'Vikas', 'Hitesh', 'Sriram', 'Lokesh', 'Gagan'])
    family = set(['Vikas', 'Hitesh', 'Shilpa', 'Mohit'])
    print(f"College friends are: {college}")
    print(f"Coworkers friends are: {coworkers}")
    print(f"Family friends are: {family}")
    print(f"All of my friends are: {college.union(coworkers, family)}")

if __name__ == '__main__':
    main()

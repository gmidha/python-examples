#!/usr/bin/env python3

# This program demonstrates the binary search whose complexity is O(n).

def binary_search(data, target, low, high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if data[mid] == target:
            return True
        elif target<data[mid]:
           return binary_search(data, target, low, mid-1)
        else:
          return binary_search(data, target, mid+1, high)

def main():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    s = binary_search(my_list, 40, 0, len(my_list)-1)
    print(s)

if __name__ == '__main__':
    main()

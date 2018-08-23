#!/usr/bin/env python3
# this program selects and displays number that are less than the input number
def get_list():
    x = int(input("Enter a number that needs to be searched: "))
    y = [ 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14 ]
    z = []
    for i in range(len(y)):
      if y[i] <= x:
          z.append(y[i])
    #for j in range(len(z)):
    #    print(f"{z[j]}")
    print(f"{z}")

if __name__ == '__main__':
    get_list()

#!/usr/bin/env python3

def cal_even_list():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [ i for i in a if i % 2 == 0 ]
    print(f"{b} is the even list")

if __name__ == "__main__":
    cal_even_list()

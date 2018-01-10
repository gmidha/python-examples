#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

def test():
    word1 = input("enter first word ")
    print(word1)
    word1_list = []
    word2_list = []
    for i in word1:
        word1_list.append(i)
    word1_list.sort()
    print(word1_list)
    word2 = input("enter second word ")
    print(word2)
    for z in word2:
        word2_list.append(z)
    word2_list.sort()
    print(word2_list)
    if word1_list == word2_list:
        print("anagram")
    else:
        print("not anagram")


if __name__ == '__main__':
    test()

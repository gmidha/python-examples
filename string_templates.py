#!/usr/bin/env python3

# This program demonstrates the usage of template with strings.

from string import Template

def main():

    str = "I am a {0}, I love coding {1}".format("coder", "python")
    print(str)
    print("--------------------------------")

    temp = Template("I am a ${x}, I love coding ${y}")
    str2=temp.substitute(x="coder", y="python")
    print(str2)
    print("--------------------------------")

    #substituting template with values from dictionaries
    data = { "x": "coder",
             "y": "python"
           }
    str3=temp.substitute(data)
    print(str3)
    print("--------------------------------")

if __name__ == "__main__":
    main()

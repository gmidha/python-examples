#!/usr/bin/env python3

# This file is being used for demonstration of JSON error handling using JSONDecodeError. We will be intentionally missing , in first line of json_string to test the program.

import json
from json import JSONDecodeError

def main():

    json_string = '''{
                        "Student" : "Chris"
                        "Subject" : "Chemistry",
                        "favt_food" : [
                                        "Ice Cream",
                                        "Cheese Sandwich",
                                        "Bean Sandwich"
                                      ],
                        "Location" : "Earth"
                     }'''
    # Use loads function to convert json string into python dict and Use try - except to catch exceptions.
    try:
        json_dict = json.loads(json_string)
        print(f"dict: {json_dict}")
        print("------------------")
        print(f"{json_dict['Student']}")
        print("------------------")
        print(f"{json_dict['Subject']}")
        print("------------------")
        print(f"{json_dict['favt_food']}")
        print("------------------")
        for food in json_dict['favt_food']:
            print(f"{food}")
    except JSONDecodeError as err:
        print(err.msg)
        print(err.lineno)
        print(err.colno)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# This file is being used for encoding/serialization of data to dump the python dict. We are using dumps() function.

import json

def main():

    json_string = '''{
                        "Student" : "Chris",
                        "Subject" : "Chemistry",
                        "favt_food" : [
                                        "Ice Cream",
                                        "Cheese Sandwich",
                                        "Bean Sandwich"
                                      ],
                        "Location" : "Earth"
                     }'''
    # Use loads function to convert json string into python dict
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

    # Use dump function to convert python dict to Json string
    str = json.dumps(json_dict, indent=4)
    print("------------------")
    print(f"{str}")


if __name__ == "__main__":
    main()

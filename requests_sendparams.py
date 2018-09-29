#!/usr/bin/env python3

# Get the status code, headers and content using requests module and passing in values as parameters

import requests

def main():
    url = "http://httpbin.org/get"
    data_values = {"Student": "Mike",
                   "Roll_id": 12
                  }
    result = requests.get(url, params=data_values)
    print(f"{result.status_code}")
    print("-----------------")
    print(f"{result.headers}")
    print("-----------------")
    print(f"{result.content}")
    print("-----------------")
    print(f"{result.text}")

if __name__ == "__main__":
    main()

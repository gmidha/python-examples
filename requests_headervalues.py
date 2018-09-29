#!/usr/bin/env python3

# Get the status code, headers and content using requests module and passing in header values as header using get method

import requests

def main():
    url = "http://httpbin.org/get"
    header_values = {"User-Agent": "Safari 1.0.0"
                  }
    result = requests.get(url, headers=header_values)
    print(f"{result.status_code}")
    print("-----------------")
    print(f"{result.headers}")
    print("-----------------")
    print(f"{result.content}")
    print("-----------------")
    print(f"{result.text}")

if __name__ == "__main__":
    main()

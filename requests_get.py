#!/usr/bin/env python3

# Get the status code, headers and content using requests module

import requests

def main():
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    print(f"{result.status_code}")
    print("-----------------")
    print(f"{result.headers}")
    print("-----------------")
    print(f"{result.content}")
    print("-----------------")
    print(f"{result.text}")

if __name__ == "__main__":
    main()

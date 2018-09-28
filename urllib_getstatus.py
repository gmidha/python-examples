#!/usr/bin/env python3

# Get the status code for url and compare it with OK from HTTPStatus

import urllib.request
from http import HTTPStatus

def main():
    url = "http://httpbin.org/html"
    result = urllib.request.urlopen(url)

    print(f"result code is {result.status}")

    #compare the status code returned by url
    if result.getcode() == HTTPStatus.OK :
        print(f"{result.read().decode('utf-8')}")

if __name__ == "__main__":
    main()

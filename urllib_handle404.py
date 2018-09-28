#!/usr/bin/env python3

# Get the status code for url, compare it with OK from HTTPStatus and handle 404 code returned by url.

import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError

def main():
    url = "http://httpbin.org/status/404"
    try:
        result = urllib.request.urlopen(url)

        print(f"result code is {result.status}")

        #compare the status code returned by url
        if result.getcode() == HTTPStatus.OK :
            print(f"{result.read().decode('utf-8')}")
    except HTTPError as err:
        print(f"Error Code is {err.code}")

if __name__ == "__main__":
    main()

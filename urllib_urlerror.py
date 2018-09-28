#!/usr/bin/env python3

# Get the status code for url, compare it with OK from HTTPStatus and handle 404 code returned by url and url is invalid.

import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    url = "http://no-such-server-exists.org"
    try:
        result = urllib.request.urlopen(url)

        print(f"result code is {result.status}")

        #compare the status code returned by url
        if result.getcode() == HTTPStatus.OK :
            print(f"{result.read().decode('utf-8')}")
    except HTTPError as err:
        print(f"Error Code is {err.code}")
    except URLError as err:
        print(f"Error reason is {err.reason}")

if __name__ == "__main__":
    main()

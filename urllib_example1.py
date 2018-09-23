#!/usr/bin/env python3

# use urllib module to request data

import urllib.request

def main():
    url = "http://httpbin.org/xml"
    response = urllib.request.urlopen(url)

    #get the response code
    print("response code is: ")
    print(f"{response.status}")
    print("------------------")

    #get the response headers
    print("response headers are: ")
    print(f"{response.getheaders()}")
    print("------------------")

    #get the response data
    print("response data is: ")
    print(f"{response.read().decode('utf-8')}")
    print("------------------")

if __name__ == "__main__":
    main()

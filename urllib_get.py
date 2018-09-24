#!/usr/bin/env python3

import urllib.request
import urllib.parse

def main():
    get_url = "https://httpbin.org/get"
    data1 = { 'Name': 'Gaurav',
              'is_coder': True
            }

    # Encoding the get parameters using urllib.parse
    encoded_data = urllib.parse.urlencode(data1)

    # Calling a get request with encoded data
    response = urllib.request.urlopen(get_url + '?' + encoded_data)

    # Getting the status code from the above response
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("Response Status code is:")
    print(f"{response.status}")
    print("++++++++++++++++++++++++++++++++++++++++++")

    # Getting the headers from the above response
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("Response Headers are:")
    print(f"{response.getheaders()}")
    print("++++++++++++++++++++++++++++++++++++++++++")

   # Getting the data from the above response
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("Response Data is:")
    print(f"{response.read()}")
    print("++++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    main()

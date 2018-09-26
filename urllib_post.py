import urllib.request
import urllib.parse

def main():
    post_url = "https://httpbin.org/post"
    data1 = { 'Name': 'Gaurav',
              'is_coder': True
            }

    # Encoding the data using parse and data.encode()
    data1 = urllib.parse.urlencode(data1)
    encoded_data = data1.encode()

    # Calling a post request with encoded data
    response = urllib.request.urlopen(post_url, data=encoded_data)

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
    
    
if __name__ == "__main__":
    main() 

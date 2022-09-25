#!/usr/bin/python3
"""
7-error_code:
    takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
Requirements:
    - If the HTTP status code is greater than or equal to 400, print:
      Error code: followed by the value of the HTTP status code
    - You must use the packages requests and sys
     -You are not allowed to import other packages than requests and sys
    - You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
import requests


def main():
    http_url = argv[1]
    response = requests.get(http_url)
    if response.status_code > 399:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()

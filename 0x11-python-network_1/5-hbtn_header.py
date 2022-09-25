#!/usr/bin/python3
"""
5-hbtn_header:
    takes in a URL, sends a request to the URL and displays the value of the
    'X-Request-Id' variable found in the header of the response.
Requirements:
    - You must use the packages requests and sys
    - You are not allow to import packages other than requests and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
import requests


def main():
    """
    get response from url
    """
    http_url = argv[1]
    respo = requests.get(http_url)
    html = dict(respo.headers).get("X-Request-Id")
    print(html)


if __name__ == "__main__":
    main()

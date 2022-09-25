#!/usr/bin/python3
"""
6-post_email:
    takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
Requirements:
    - The email must be sent in the email variable
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
import requests


def main():
    """
    post the email to the given address
    """
    http_url = argv[1]
    email = argv[2]
    value = {"email": email}
    respo = requests.post(http_url, data=value)
    print(respo.text)


if __name__ == "__main__":
    main()

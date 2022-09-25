#!/usr/bin/python3
"""
10-my_github:
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
Requirements:
    - You must use Basic Authentication with a personal access token as
      password to access to your information
      (only read:user permission is needed)
    - The first argument will be your username
    - The second argument will be your password
      (in your case, a personal access token as password)
    - You must use the package requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don’t need to check arguments passed to the script(number or type)
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def main():
    user = argv[1]
    passwd = argv[2]
    url = "https://api.github.com/user"
    respo = requests.get(url, auth=HTTPBasicAuth(user, passwd))
    print(respo.json().get("id"))


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
100-github_commits:
    takes 2 arguments in order to solve this challenge.
Requirements:
    - The first argument will be the repository name
    - The second argument will be the owner name
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don’t need to check arguments passed to the script(number or type)
"""
import requests
from sys import argv


def main():
    repo_name = argv[1]
    repo_owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            repo_owner, repo_name)
    respo = requests.get(url)
    commits = respo.json()
    for commit in commits:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))


if __name__ == "__main__":
    main()

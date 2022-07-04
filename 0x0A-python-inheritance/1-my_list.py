#!/usr/bin/python3
"""
1-my_list.py
inherits from list
"""


class MyList(list):
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))

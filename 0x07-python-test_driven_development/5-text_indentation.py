#!/usr/bin/python3
"""
5-text_indentation.py
 prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    let_str = "".join([let + "\n\n" if let in "?.:" else let for let in text])
    print("\n".join([line.strip() for line in let_str.split("\n")]), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

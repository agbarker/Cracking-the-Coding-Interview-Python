"""Write a method to replace all spaces in a string with '%20'.  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string."""

"""Replacement in place is not possible in python as strings are immutable.  Much of the input is unecessary in python due to this constraint.  I have eliminated the length variable input."""

def urlify(string):
    """Converts string with spaces to valid url.

    >>> urlify('taco cat')
    'taco%20cat'

    >>> urlify('cat')
    'cat'"""

    tokens = string.split(" ")

    i = 1
    result = tokens[0]

    while i in range(len(tokens)):
        result = result + '%20' + tokens[i]
        i += 1

    return result

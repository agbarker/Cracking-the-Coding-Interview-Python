"""Implement an algorithm to determine if a string has all unque characters.  What if you cannot use additional data structures?"""

"""An obvious choice would be to convert the string to a list, the list to a set, and compare the length of the set to the length of the list.  If they are they same, the string is unique."""

"""The most brute force way would be to iterate through each character and compare it to every other characters.  This can be optimized by only comparing it to the characters after it, reducing runtime from O(n^2) to O(nlog n)"""

def check_unique_iter(string):
    """Checks if string contains unique characters iteratively.

    >>> check_unique_iter("cat")
    True
    >>> check_unique_iter("baboon")
    False"""

    for i, char in enumerate(string):
        if char in string[i+1:]:
            return False

    return True


def check_unique_recurs(string):
    """Checks if string contains unique characters recursively.

    >>> check_unique_iter("cat")
    True
    >>> check_unique_iter("baboon")
    False"""

    
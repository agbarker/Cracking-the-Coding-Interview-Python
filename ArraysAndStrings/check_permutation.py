"""Given two strings, write a method to decide if one is a permutation of the other."""

def check_anagram_iter(string1, string2):
    """Checks if two strings are anagrams.

    >>> check_anagram_iter("cat", "tac")
    True

    >>> check_anagram_iter("cat", "baboon")
    False

    >>> check_anagram_iter("", "")
    True"""


    #checks if words are different length, automatic fail
    if len(string1) != len(string2):
        return False

    #turns strings into lists and sorts them
    a = sorted(string1)
    b = sorted(string2)

    done_checking = False

    while not done_checking:
        if not a or not b:
            done_checking = True
            break

        if a[0] == b[0]:
            a.pop(0)
            b.pop(0)
        else:
            return False

    return True

def check_anagram_recurs(string1, string2):
    """Checks if two strings are anagrams.

    >>> check_anagram_recurs("cat", "tac")
    True

    >>> check_anagram_recurs("cat", "baboon")
    False

    >>> check_anagram_recurs("", "")
    True"""

    a = sorted(string1)
    b = sorted(string2)

    if not a or not b:
        return True

    if a[0] == b[0]:
        return check_anagram_recurs(a[1:], b[1:])
    else:
        return False


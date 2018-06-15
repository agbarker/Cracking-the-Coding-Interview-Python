"""There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.  Given two strings, write a function to check if they are one edit (or zero edits) away."""


def check_one_away(string1, string2):
    """Checks if two strings are one or less edit away from each other.

    >>> check_one_away("pale", "ple")
    True

    >>> check_one_away("pales", "pale")
    True

    >>> check_one_away("pale", "bale")
    True

    >>> check_one_away("pale", "bake")
    False

    >>> check_one_away("ants", "aunties")
    False"""

    #check greater difference of length
    if abs(len(string1) - len(string2)) > 1:
        return False


    #a is always be the longer string
    if len(string1) >= len(string2):
        a = string1
        b = string2
    else:
        a = string2
        b = string1

    edits_counter = 0

    i = 0
    j = 0

    #check for one deletion
    if len(a) > len(b):
        for i in range(len(a) -1):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                if edits_counter > 0:
                    return False
                else:
                    edits_counter += 1
                    i += 1

    #check for one substitution
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                if edits_counter > 0:
                    return False
                else:
                    edits_counter += 1
                    i += 1
                    j += 1

    return True




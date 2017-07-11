
# 1.5
# One Away
#
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.
#


def levdis (s1 : str, s2 : str) -> int :
    m = len (s1) + 1
    n = len (s2) + 1

    d = [[0 for _ in range (n + 1)] for _ in range (m + 1)]

    for i in range (1, m) :
        d [i] [0] = i

    for j in range (1, n) :
        d [0] [j] = j

    for j in range (1, n) :
        for i in range (1, m) :
            if   s1 [i - 1] == s2 [j - 1] :
                d [i] [j] = d [i - 1] [j - 1]
            else :
                d [i] [j] = min (d [i - 1] [j], d [i] [j - 1], d [i - 1] [j - 1]) + 1

    return d [m - 1] [n - 1]


def sol1 (s1 : str, s2 : str) -> bool :
    dis = levdis (s1, s2)

    return dis == 0 or dis == 1


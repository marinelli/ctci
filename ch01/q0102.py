
# 1.2
# Check Permutation
#
# Given two strings, write a method to decide if one
# is a permutation of the other.
#


def sol1 (s1 : str, s2 : str) -> bool :
    return sorted (s1) == sorted (s2)


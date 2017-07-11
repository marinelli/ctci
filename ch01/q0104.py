
# 1.4
# Palindrome Permutation
#
# Given a string, write a function to check if it is a permutation
# of a palindrome. A palindrome is a word or phrase that is the same
# forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
#


from collections import Counter


def sol1 (s : str) -> bool :
    purged_s      = (('').join (s.split ())).lower ()
    chars_of_s    = (Counter (purged_s)).values ()
    how_many_odds = len (list (filter (lambda x : x % 2 == 1, chars_of_s)))

    return how_many_odds == 0 or how_many_odds == 1


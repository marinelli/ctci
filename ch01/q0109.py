
# 1.9
# String Rotation
#
# Assumeyou have a method isSubstringwhich checks ifoneword isa
# substring of another. Given two strings, sl and s2, write code to
# check if s2 is a rotation of sl using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of"erbottlewat").
#


def sol1 (s1 : str, s2 : str) -> bool :
    return s2 in (s1 + s1)



# 1.1
# Is Unique
#
# Implement an algorithm to determine if a string has all unique
# characters. What if you cannot use additional data structures?
#


def sol1 (s) :
    return len (s) == len (set (s))


def sol2 (s) :
    sorted_s = sorted (s)

    for i in range (len (sorted_s) - 1) :
        if sorted_s [i] == sorted_s [i + 1] :
            return False

    return True


def sol3 (s) :
    sorted_s = sorted (s)

    for x, y in zip (sorted_s [:-1], sorted_s [1:]) :
        if x == y :
            return False

    return True


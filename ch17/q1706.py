
# 17.2
# Count of 2s
#
# Write a method to count the number of 2s that appear in all the
# numbers between 0 and n (inclusive).
#


from math import floor, log10



def sol1 (n) :

    if n < 0 :
        raise ValueError

    result = 0

    for i in range (n + 1) :

        q = i

        for _ in range (1 + floor (log10 (n))) :

            q, r = divmod (q, 10)

            if r == 2 :
                result = result + 1

    return result



def sol2 (n) :

    if n < 0 :
        raise ValueError

    result = 0

    for i in range (n + 1) :

        result = result + len (list (filter (lambda x : x == str (2), (list (str (i))))))

    return result


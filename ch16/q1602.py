
# 16.2
# Word Frequencies
#
# Design a method to find the frequency of occurrences of any given
# word in a book. What if we were running this algorithm multiple
# times?
#


from collections import Counter

from itertools import groupby



def sol1 (book) :
    words = (book.lower ()).split ()
    return dict ([(x, len (list (y))) for x, y in groupby (sorted (words))])



def sol2 (book) :
    result = dict ()

    for w in (book.lower ()).split () :
        result.update ([(w, 1 + result.get (w, 0))])

    return result



def sol3 (book) :
    return dict (Counter ((book.lower ()).split ()))


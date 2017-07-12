
# 1.6
# String Compression
#
# Implement a method to perform basic string compression using the
# counts of repeated characters. For example, the string aabcccccaaa
# would become a2blc5a3. If the "compressed" string would not become
# smaller than the original string, your method should return the
# original string. You can assume the string has only uppercase and
# lowercase letters (a - z).
#


from common import fst, snd


def sol1 (s : str) -> str :

    l = [None] + list (s) + [None]

    result   = []
    cur_char = None
    counter  = 0

    for p in zip (l [:-1], l [1:]) :

        if fst (p) == snd (p) :
            counter = counter + 1
        else :
            result.append ((cur_char, counter))
            cur_char = snd (p)
            counter  = 1

    result = ('').join (map (lambda p : fst (p) + str (snd (p)), result [1:] ))

    if len (result) < len (s) :
        return result
    else :
        return s


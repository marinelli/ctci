

def fst (p) :
    return p [0]


def snd (p) :
    return p [1]


def sol1 (s : str) -> str :

    l = [None] + list (s) + [None]

    result   = []
    cur_char = None
    counter  = 0

    for p in zip (l [:-1], l [1:]) :

        if   fst (p) == None :
            cur_char = snd (p)
            counter = 1
        elif fst (p) == snd (p) :
            counter = counter + 1
        else :
            result.append ((cur_char, counter))
            cur_char = snd (p)
            counter  = 1

    result = ('').join (map (lambda p : fst (p) + str (snd (p)), result))

    if len (result) < len (s) :
        return result
    else :
        return s


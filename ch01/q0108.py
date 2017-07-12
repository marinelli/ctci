
# 1.8
# Zero Matrix
#
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
#


from common import fst, snd


def sol1 (matrix) :
    if matrix == [] :
        return []

    m_rows       = len (matrix)
    n_columns    = len (matrix [0])

    coordinates  = [(x, y) for x in range (m_rows) for y in range (n_columns)]

    zeros        = list (filter (lambda p : matrix [fst (p)] [snd (p)] == 0, coordinates))

    zero_rows    = set (map (fst, zeros))
    zero_columns = set (map (snd, zeros))

    result = [ [ 0 if (i in zero_rows or j in zero_columns) else matrix [i] [j]
                 for j in range (n_columns)
               ]
               for i in range (m_rows)
             ]

    return result


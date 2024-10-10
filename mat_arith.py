# There is no need to import SAMPLE_MATRICES
# Luke Brudnok
# 10/8/24


def mat_sum(m1, m2):
    if len(m1) != len(m2):
        return "no solution"
    if len(m1[0]) != len(m2[0]):
        return "no solution"

    height = len(m1)
    width = len(m1[0])

    new = [[0]*width for i in range(height)]
    for r in range(height):
        for el in range(width):
            new[r][el] = m1[r][el] + m2[r][el]
    
    return new



def mat_mul(m1, m2):
    m1row = len(m1)
    m1column = len(m1[0])
    m2row = len(m2)
    m2column = len(m2[0])

    if m1column != m2row:
        return "no solution"
    
    new = [[0]*m2column for i in range(m1row)]
    for r in range(m1row):
        for x in range(m2column):
            for el in range(m2row):
                new[r][x] += m1[r][el] * m2[el][x]
            
            #math stuff
    return new
